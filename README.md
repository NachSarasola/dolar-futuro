# Dólar Futuro Copiloto

Copiloto de trading profesional para futuros de dólar (Matba-Rofex).
Enfoque en robustez, performance y experiencia de desarrollador limpia.

## Arquitectura

Monorepo con las siguientes carpetas:

- `apps/backend`: FastAPI 3.11 con modelos pydantic y endpoints.
- `apps/web`: Next.js 14 con TypeScript y Tailwind.
- `packages/shared`: esquemas y tipos compartidos.
- `infra`: Docker Compose, base de datos y utilidades.

## Reglas generales

- No se envían órdenes reales por defecto.
- Configuración por `.env` o UI.
- Registrar todas las decisiones de la estrategia.

## Roadmap

1. Bootstrap inicial del proyecto.
2. Backend mínimo con endpoints mock.
3. Frontend básico con dashboard.
4. Señales y cálculo de Score de intervención.
5. Sizing y control de riesgo.
6. Ejecución segura y guardrails.
7. Conectores de datos y TimescaleDB.

## Desarrollo

```
make setup  # instala dependencias básicas
make dev    # arranca backend en modo desarrollo
make test   # ejecuta tests
```

## Licencia

MIT
