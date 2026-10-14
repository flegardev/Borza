import secrets

import pytest
from pydantic import ValidationError

from app.core.config import Settings


@pytest.mark.parametrize("environment", ["preview", "staging", "production"])
@pytest.mark.parametrize(
    "secret",
    [
        None,
        "local-development-classroom-secret-change-me",
        " local-development-classroom-secret-change-me ",
        "too-short",
        " " * 32,
    ],
)
def test_deployed_classroom_secret_rejects_unsafe_values(
    monkeypatch, environment: str, secret: str | None
) -> None:
    monkeypatch.delenv("CLASSROOM_CODE_SECRET", raising=False)
    kwargs = {} if secret is None else {"classroom_code_secret": secret}
    with pytest.raises(ValidationError, match="CLASSROOM_CODE_SECRET"):
        Settings(
            _env_file=None,
            environment=environment,
            database_url="postgresql+psycopg://user:pass@db.example.test/academy",
            migration_database_url="postgresql+psycopg://user:pass@db.example.test/academy",
            supabase_url="https://project.supabase.co",
            supabase_publishable_key="publishable-test-key",
            **kwargs,
        )


@pytest.mark.parametrize("environment", ["preview", "staging", "production"])
def test_deployed_classroom_secret_accepts_custom_value(environment: str) -> None:
    # An ephemeral 32-character fixture, never an operational signing key.
    secret = secrets.token_urlsafe(24)
    settings = Settings(
        _env_file=None,
        environment=environment,
        database_url="postgresql+psycopg://user:pass@db.example.test/academy",
        migration_database_url="postgresql+psycopg://user:pass@db.example.test/academy",
        supabase_url="https://project.supabase.co",
        supabase_publishable_key="publishable-test-key",
        classroom_code_secret=secret,
    )
    assert settings.classroom_code_secret.get_secret_value() == secret


@pytest.mark.parametrize("environment", ["development", "test"])
def test_local_classroom_secret_default_remains_supported(monkeypatch, environment: str) -> None:
    monkeypatch.delenv("CLASSROOM_CODE_SECRET", raising=False)
    settings = Settings(_env_file=None, environment=environment)
    assert settings.classroom_code_secret.get_secret_value() == (
        "local-development-classroom-secret-change-me"
    )


def test_invalid_runtime_does_not_print_connection_or_auth_secrets() -> None:
    with pytest.raises(ValidationError, match="CLASSROOM_CODE_SECRET") as error:
        Settings(
            _env_file=None,
            environment="production",
            database_url="postgresql+psycopg://user:private-database-marker@db.example.test/academy",
            migration_database_url=(
                "postgresql+psycopg://user:private-migration-marker@db.example.test/academy"
            ),
            supabase_url="https://project.supabase.co",
            supabase_publishable_key="private-auth-marker",
            classroom_code_secret="short-private-marker",
        )
    message = str(error.value)
    assert "private-database-marker" not in message
    assert "private-migration-marker" not in message
    assert "private-auth-marker" not in message
    assert "short-private-marker" not in message
