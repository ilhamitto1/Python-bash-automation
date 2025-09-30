#!/bin/bash
LOG_DIR="$1"
BACKUP_DIR="${2:-$HOME/log_backups}"

mkdir -p "$BACKUP_DIR"

shopt -s nullglob
for file in "$LOG_DIR"/*.log; do
  cp "$file" "$BACKUP_DIR/${file##*/}.$(date +%Y%m%d%H%M%S).bak"
  : > "$file"
  echo "Cleaned: $file -> backup created"
done
