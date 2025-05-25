# param_store.py
import os, json, urllib.request, http.client

_IS_LOCAL = bool(os.getenv("BODYSTAT_LOCAL"))
_STAGE    = os.getenv("BODYSTAT_STAGE", "test")
_APP      = "body-stat-bot"
_TOKEN    = os.getenv("AWS_SESSION_TOKEN")
_BASE     = "http://localhost:2773"

def _ssm_path(key: str) -> str:
    return f"/{_STAGE}/{_APP}/{key}"

def _via_extension(path: str) -> str:
    if not _TOKEN:
        raise RuntimeError("AWS_SESSION_TOKEN is missing")
    url = f"{_BASE}/systemsmanager/parameters/get?name={path}&withDecryption=true"
    req = urllib.request.Request(url, headers={"X-Aws-Parameters-Secrets-Token": _TOKEN})
    body = urllib.request.urlopen(req, timeout=1).read()
    return json.loads(body)["Parameter"]["Value"]

def get_param(key: str, *, default=None) -> str:
    if _IS_LOCAL:
        val = os.getenv(key)
        if val is not None:
            return val
        if default is not None:
            return default
        raise RuntimeError(f"{key} not set in local environment")
    try:
        return _via_extension(_ssm_path(key))
    except Exception:
        if default is not None:
            return default
        raise
