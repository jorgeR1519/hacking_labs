-- Inicialización de base de datos simulando Snowflake
CREATE TABLE IF NOT EXISTS customer_data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    phone VARCHAR(20),
    credit_card VARCHAR(30),
    ssn VARCHAR(11),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS financial_records (
    id SERIAL PRIMARY KEY,
    customer_id INT,
    transaction_date DATE,
    amount DECIMAL(10,2),
    account_number VARCHAR(50),
    routing_number VARCHAR(50),
    bank_name VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS employee_info (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(50),
    full_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(12,2),
    email VARCHAR(150),
    hire_date DATE
);

CREATE TABLE IF NOT EXISTS api_keys (
    id SERIAL PRIMARY KEY,
    service_name VARCHAR(100),
    api_key VARCHAR(256),
    secret_key VARCHAR(256),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo
INSERT INTO customer_data (name, email, phone, credit_card, ssn, address) VALUES
('Juan Pérez', 'juan.perez@email.com', '+1-555-0101', '4111-1111-1111-1111', '123-45-6789', '123 Main St, NY'),
('María García', 'maria.garcia@email.com', '+1-555-0102', '5500-0000-0000-0004', '987-65-4321', '456 Oak Ave, LA'),
('Empresa ABC', 'info@abc.com', '+1-555-0103', '3782-822463-10005', '456-78-9123', '789 Business Blvd, Chicago');

INSERT INTO financial_records (customer_id, transaction_date, amount, account_number, routing_number, bank_name) VALUES
(1, '2024-01-15', 1500.00, '001234567890', '021000021', 'Chase Bank'),
(2, '2024-02-20', 2500.50, '009876543210', '121000358', 'Bank of America'),
(1, '2024-03-10', -500.00, '001234567890', '021000021', 'Chase Bank');

INSERT INTO employee_info (employee_id, full_name, department, salary, email, hire_date) VALUES
('EMP001', 'Carlos Rodríguez', 'IT', 85000.00, 'carlos.rodriguez@company.com', '2020-06-15'),
('EMP002', 'Ana Martínez', 'HR', 72000.00, 'ana.martinez@company.com', '2019-03-22'),
('EMP003', 'Robert Smith', 'Finance', 95000.00, 'robert.smith@company.com', '2021-11-30');

INSERT INTO api_keys (service_name, api_key, secret_key) VALUES
('Payment Gateway', 'sk_live_4eC39HqLyjWDarjtT1zdp7dc', 'whsec_5eC39HqLyjWDarjtT1zdp7dc'),
('Cloud Storage', 'AKIAIOSFODNN7EXAMPLE', 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'),
('Database Access', 'snowflake_sim_key_2024', 'super_secret_key_do_not_share');

-- Crear usuario sin MFA (simulando configuración vulnerable)
CREATE USER insecure_user WITH PASSWORD 'Password123';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO insecure_user;

-- Tabla de logs de auditoría
CREATE TABLE IF NOT EXISTS security_logs (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    event_type VARCHAR(50),
    username VARCHAR(100),
    ip_address VARCHAR(45),
    details TEXT
);

CREATE INDEX idx_security_logs_time ON security_logs(event_time);
