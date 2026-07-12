import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "ecosystem-documentation-endpoints.json"
HEALTH = ROOT / "data" / "cross-wiki-health-status.json"
HEALTH_SCHEMA = ROOT / "data" / "cross-wiki-health-status.schema.json"
COMPLETION = ROOT / "data" / "wiki-completion-status.json"
EXPECTED_ENDPOINTS = {
    "stegverse-site": ("StegVerse-Labs/Site", "https://stegverse-labs.github.io/Site/"),
    "admissibility-wiki": ("StegVerse-Labs/admissibility-wiki", "https://stegverse-labs.github.io/admissibility-wiki/"),
    "stegguardian-wiki": ("StegVerse-002/stegguardian-wiki", "https://stegverse-002.github.io/stegguardian-wiki/"),
    "stegtalk-wiki": ("StegVerse-Labs/stegtalk-wiki", "https://stegverse-labs.github.io/stegtalk-wiki/"),
}


def load_json(path: Path, errors: list[str], label: str) -> dict:
    if not path.exists():
        errors.append("missing_" + label)
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(label + "_json_error:" + str(exc))
        return {}


def main() -> int:
    errors: list[str] = []
    registry = load_json(REGISTRY, errors, "endpoint_registry")
    health = load_json(HEALTH, errors, "health_status")
    schema = load_json(HEALTH_SCHEMA, errors, "health_schema")
    completion = load_json(COMPLETION, errors, "completion_status")

    if registry.get("record_type") != "stegverse_ecosystem_documentation_endpoints":
        errors.append("endpoint_registry_type_mismatch")
    endpoints = {item.get("id"): item for item in registry.get("endpoints", [])}
    for endpoint_id, (repo, url) in EXPECTED_ENDPOINTS.items():
        item = endpoints.get(endpoint_id)
        if not item:
            errors.append("missing_endpoint:" + endpoint_id)
            continue
        if item.get("repo") != repo:
            errors.append("endpoint_repo_mismatch:" + endpoint_id)
        if item.get("url") != url:
            errors.append("endpoint_url_mismatch:" + endpoint_id)

    if schema.get("title") != "StegVerse Cross-Wiki Health Status":
        errors.append("health_schema_title_mismatch")
    if schema.get("properties", {}).get("schema_version", {}).get("const") != "1.0.0":
        errors.append("health_schema_version_mismatch")
    required = set(schema.get("required", []))
    for field in ("schema_ref", "peer_registry", "checks", "next_actions", "non_claims"):
        if field not in required:
            errors.append("health_schema_missing_required:" + field)

    if health.get("schema_version") != "1.0.0":
        errors.append("health_schema_version_binding_mismatch")
    if health.get("schema_ref") != "data/cross-wiki-health-status.schema.json":
        errors.append("health_schema_ref_mismatch")
    if health.get("record_type") != "stegtalk_cross_wiki_health_status":
        errors.append("health_record_type_mismatch")
    if health.get("repo") != "StegVerse-Labs/stegtalk-wiki":
        errors.append("health_repo_mismatch")
    if health.get("origin_public_url") != "https://stegverse-labs.github.io/stegtalk-wiki/":
        errors.append("health_origin_url_mismatch")
    if health.get("peer_registry") != "data/ecosystem-documentation-endpoints.json":
        errors.append("health_peer_registry_mismatch")
    if health.get("status") != "pending_live_peer_checks":
        errors.append("health_status_must_remain_pending_until_verified")

    checks = health.get("checks", {})
    if checks.get("peer_urls_declared") is not True:
        errors.append("peer_urls_declared_must_be_true")
    if checks.get("origin_records_declared") is not True:
        errors.append("origin_records_declared_must_be_true")
    for key in (
        "live_peer_http_confirmed",
        "peer_machine_records_confirmed",
        "cross_wiki_schema_consistency_confirmed",
    ):
        if checks.get(key) is not False:
            errors.append("check_must_remain_false_until_verified:" + key)

    non_claims = health.get("non_claims", {})
    for key in ("cross_repo_authority_granted", "standing_conferred", "execution_authority"):
        if non_claims.get(key) is not False:
            errors.append("health_non_claim_must_remain_false:" + key)

    if completion.get("record_type") != "stegtalk_wiki_completion_status":
        errors.append("completion_record_type_mismatch")
    if completion.get("repo") != "StegVerse-Labs/stegtalk-wiki":
        errors.append("completion_repo_mismatch")
    if completion.get("public_url") != "https://stegverse-labs.github.io/stegtalk-wiki/":
        errors.append("completion_public_url_mismatch")
    completion_values = completion.get("completion", {})
    for key in (
        "publishing_automation",
        "page_indexing",
        "documentation_mesh_registry",
        "cross_wiki_health_scaffolding",
        "substantive_page_expansion",
        "page_level_evidence_notes",
        "overall_repo_goal",
    ):
        value = completion_values.get(key)
        if not isinstance(value, int) or not 0 <= value <= 100:
            errors.append("invalid_completion_value:" + key)

    if errors:
        print("STEGTALK DOCUMENTATION MESH: FAIL - " + ", ".join(errors))
        return 1
    print("STEGTALK DOCUMENTATION MESH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
