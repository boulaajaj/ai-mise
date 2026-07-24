# Repository mind map (generated)

<!-- GENERATED FILE - do not edit. Regenerate: python tools/generate_mindmap.py (ADR-0006) -->

Nodes: 29 markdown files · Edges: 50 links · The link graph inside the files is the source of truth; this is only a rendered view.

```mermaid
graph LR
  subgraph _github_g[.github]
    _github_copilot_instructions_md["copilot-instructions"]
    _github_instructions_docs_instructions_md["docs.instructions"]
    _github_instructions_validators_instructions_md["validators.instructions"]
  end
  subgraph control_plane_g[control-plane]
    control_plane_evaluation_baselines_README_md["baselines/README"]
    control_plane_threat_tests_scenarios_md["scenarios"]
  end
  subgraph docs_g[docs]
    docs_GLOSSARY_md["GLOSSARY"]
    docs_architecture_md["architecture"]
    docs_decisions_ADR_0001_control_plane_separation_md["ADR-0001-control-plane-separation"]
    docs_decisions_ADR_0002_evidence_claims_views_md["ADR-0002-evidence-claims-views"]
    docs_decisions_ADR_0003_shadow_mode_self_improvement_md["ADR-0003-shadow-mode-self-improvement"]
    docs_decisions_ADR_0004_claim_hygiene_md["ADR-0004-claim-hygiene"]
    docs_decisions_ADR_0005_builder_vs_workspace_md["ADR-0005-builder-vs-workspace"]
    docs_decisions_ADR_0006_formats_over_tools_md["ADR-0006-formats-over-tools"]
    docs_decisions_ADR_0007_challenge_before_compliance_md["ADR-0007-challenge-before-compliance"]
    docs_decisions_ADR_0008_no_modes_tiered_application_md["ADR-0008-no-modes-tiered-application"]
    docs_decisions_ADR_0009_domain_language_and_structure_md["ADR-0009-domain-language-and-structure"]
    docs_dependencies_md["dependencies"]
    docs_deployment_md["deployment"]
    docs_foundations_md["foundations"]
    docs_history_blueprint_v1_md["blueprint-v1"]
    docs_meta_dev_harness_md["dev-harness"]
    docs_meta_direction_md["direction"]
    docs_meta_retro_log_md["retro-log"]
    docs_prior_art_md["prior-art"]
  end
  CLAUDE_md["CLAUDE"]
  HANDOFF_md["HANDOFF"]
  METHOD_md["METHOD"]
  README_md["repo/README"]
  subgraph skills_g[skills]
    skills_inspector_SKILL_md["SKILL"]
  end
  _github_copilot_instructions_md --> control_plane_threat_tests_scenarios_md
  _github_copilot_instructions_md --> docs_GLOSSARY_md
  _github_copilot_instructions_md --> docs_decisions_ADR_0009_domain_language_and_structure_md
  _github_copilot_instructions_md --> docs_dependencies_md
  _github_copilot_instructions_md --> docs_meta_retro_log_md
  _github_instructions_docs_instructions_md --> docs_dependencies_md
  _github_instructions_docs_instructions_md --> docs_meta_retro_log_md
  CLAUDE_md --> HANDOFF_md
  CLAUDE_md --> control_plane_threat_tests_scenarios_md
  CLAUDE_md --> docs_architecture_md
  CLAUDE_md --> docs_dependencies_md
  CLAUDE_md --> docs_deployment_md
  CLAUDE_md --> docs_meta_dev_harness_md
  CLAUDE_md --> docs_prior_art_md
  HANDOFF_md --> CLAUDE_md
  HANDOFF_md --> control_plane_threat_tests_scenarios_md
  HANDOFF_md --> docs_architecture_md
  HANDOFF_md --> docs_history_blueprint_v1_md
  HANDOFF_md --> docs_meta_dev_harness_md
  HANDOFF_md --> docs_meta_retro_log_md
  HANDOFF_md --> skills_inspector_SKILL_md
  METHOD_md --> docs_foundations_md
  README_md --> CLAUDE_md
  README_md --> HANDOFF_md
  README_md --> METHOD_md
  README_md --> docs_architecture_md
  README_md --> docs_decisions_ADR_0005_builder_vs_workspace_md
  README_md --> docs_decisions_ADR_0008_no_modes_tiered_application_md
  README_md --> docs_prior_art_md
  docs_GLOSSARY_md --> METHOD_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0001_control_plane_separation_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0002_evidence_claims_views_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0003_shadow_mode_self_improvement_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0005_builder_vs_workspace_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0007_challenge_before_compliance_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0008_no_modes_tiered_application_md
  docs_GLOSSARY_md --> docs_decisions_ADR_0009_domain_language_and_structure_md
  docs_architecture_md --> docs_history_blueprint_v1_md
  docs_decisions_ADR_0006_formats_over_tools_md --> docs_dependencies_md
  docs_decisions_ADR_0007_challenge_before_compliance_md --> _github_copilot_instructions_md
  docs_decisions_ADR_0008_no_modes_tiered_application_md --> control_plane_threat_tests_scenarios_md
  docs_decisions_ADR_0008_no_modes_tiered_application_md --> docs_decisions_ADR_0005_builder_vs_workspace_md
  docs_decisions_ADR_0008_no_modes_tiered_application_md --> docs_decisions_ADR_0007_challenge_before_compliance_md
  docs_decisions_ADR_0009_domain_language_and_structure_md --> docs_GLOSSARY_md
  docs_foundations_md --> METHOD_md
  docs_history_blueprint_v1_md --> docs_architecture_md
  docs_meta_dev_harness_md --> CLAUDE_md
  docs_meta_dev_harness_md --> docs_meta_retro_log_md
  docs_meta_direction_md --> METHOD_md
  docs_meta_retro_log_md --> docs_meta_dev_harness_md
```
