#!/bin/sh

# Esperar a que la base de datos esté lista
echo "⌛ Esperando a que la base de datos esté lista en $DB_HOST:$DB_PORT..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "✅ Base de datos disponible. Levantando Django..."

# Ejecutar el comando que sigue (pasado como argumentos al script)
exec "$@"
