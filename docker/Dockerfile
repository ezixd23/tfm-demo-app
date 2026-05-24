# ==============================================================
# Dockerfile - Secure Version
# Multi-stage build with updated and minimal base image
# Passes Trivy and Grype scans without critical/high vulnerabilities.

# ===========================================================

# Stage 1: builder
FROM python:3.12-slim AS builder

WORKDIR /build

COPY app/requirements.txt .

RUN pip install --no-cache-dir --user --upgrade pip && \
    pip install --no-cache-dir --user -r requirements.txt

# Stage 2: runtime
FROM python:3.12-slim

# Create non-root user (defense in depth - consistent with policy P1)
RUN groupadd -r -g 10001 appuser && \
    useradd -r -u 10001 -g appuser appuser

WORKDIR /app

# Copy dependencies from the builder
COPY --from=builder --chown=appuser:appuser /root/.local /home/appuser/.local

# Copy application code
COPY --chown=appuser:appuser app/app.py /app/

# Configure the PATH to access the installed binaries with --user
ENV PATH="/home/appuser/.local/bin:${PATH}" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

USER appuser

EXPOSE 8080

CMD ["python", "/app/app.py"]
