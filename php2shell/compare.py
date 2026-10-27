
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

TARGETS = {
    "vulnerable": {
        "url": "http://127.0.0.1:8086",
        "expected_version": "8.2.34",
    },
    "patched": {
        "url": "http://127.0.0.1:8087",
        "expected_version": "8.2.35",
    },
}


def get_json(url):
    with urlopen(url, timeout=5) as response:
        return response.status, json.load(response)


def inspect(name, config):
    base = config["url"]

    status, info = get_json(base + "/?format=json")
    session_status, session = get_json(base + "/sessions.php")

    checks = {
        "http_ok": status == 200,
        "expected_version": (
            info.get("php") == config["expected_version"]
        ),
        "mod_php": info.get("sapi") == "apache2handler",
        "session_http_ok": session_status == 200,
        "session_active": session.get("session_active") is True,
        "session_cookie_name": (
            session.get("session_cookie_name") == "PHPSESSID"
        ),
    }

    return {
        "target": name,
        "php_version": info.get("php"),
        "sapi": info.get("sapi"),
        "memory_limit": info.get("memory_limit"),
        "checks": checks,
        "passed": all(checks.values()),
    }


def main():
    results = []

    for name, config in TARGETS.items():
        try:
            result = inspect(name, config)
        except Exception as exc:
            result = {
                "target": name,
                "passed": False,
                "error": str(exc),
            }

        results.append(result)

        state = "PASS" if result["passed"] else "FAIL"
        print(f"[{state}] {name}: {result.get('php_version', 'N/A')}")

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "purpose": "PHP runtime baseline comparison",
        "cve_exploitation_demonstrated": False,
        "results": results,
    }

    Path("reports").mkdir(exist_ok=True)
    output = Path("reports/baseline.json")

    output.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8",
    )

    print(f"\nInforme generado: {output}")


if __name__ == "__main__":
    main()
