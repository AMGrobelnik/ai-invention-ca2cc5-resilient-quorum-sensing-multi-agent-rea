# gen_paper_text — test_idea

> Phase: `invention_loop` · round 1 · `gen_paper_text`
> Run: `run_om2tRiXGCTOe` — Resilient Quorum-Sensing Multi-Agent Reasoning with Quadratic Damping and WAN Packet-Drop Resilience
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-01 15:14:30 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<hypothesis>
The research hypothesis.

kind: hypothesis
title: Stabilized Quorum-Sensing Multi-Agent Reasoning
hypothesis: >-
  Governing decentralized multi-agent LLM model escalation through discrete-time autoinduction recurrence relations with degradation
  damping (quorum quenching), self-consistency entropy uncertainty signals, concrete prompt paraphrase sets (synonym substitution
  and structural rephrasing), explicit capability/cost matrices for heterogeneous agent pairs (e.g., Llama-3-8B base vs. Claude-3.5-Sonnet
  reasoner), multi-seed empirical validation, stability verification, and token-matched hierarchical and reflexive baselines
  optimizes Pareto efficiency across diverse reasoning benchmark classes without runaway escalation cascades.
motivation: >-
  Multi-agent LLM systems struggle with token expenditure spikes and variance from self-consistency sample noise and prompt
  phrasing. Addressing reviewer feedback by specifying concrete prompt paraphrase methods and explicit capability/cost matrices
  for heterogeneous agents establishes robust reproducibility and true Pareto dominance under extreme message frequency spikes.
assumptions:
- >-
  Multi-seed evaluations across random seeds yield reliable mean and variance estimates for Pareto efficiency curves of accuracy
  versus token expenditure.
- >-
  Theoretical stability bounds for degradation damping (quorum quenching) remain robust under heavy prompt-length variance
  and heterogeneous agent capabilities.
- >-
  Token-matched hierarchical and reflexive baselines provide rigorous comparative standards for evaluating collective density-dependent
  phase transitions.
- >-
  Self-consistency entropy across multi-sample generation scores, combined with message token weighting and explicit agent
  cost matrices, accurately captures epistemic uncertainty.
investigation_approach: >-
  Implement multi-agent simulations across diverse reasoning benchmark classes (math and code generation) with multi-seed
  runs reporting mean and variance. Test degradation rates, Hill coefficients, and explicit agent heterogeneity (pairing Llama-3-8B
  base models with Claude-3.5-Sonnet advanced reasoners under defined capability/cost matrices) across prompt paraphrase sets
  (synonym substitution and structural rephrasing). Benchmark against static routing, centralized routers, decentralized independent
  thresholds, and recent token-matched hierarchical and reflexive baselines, incorporating strict token-matched context accounting
  and conceptual architecture specifications.
success_criteria: >-
  Stabilized quorum-sensing routing achieves statistically significant Pareto efficiency gains (mean and variance across random
  seeds) over static, centralized, independent, hierarchical, and reflexive baselines, maintaining proven stability under
  extreme message frequency spikes and heavy prompt variance with explicit perturbation sets and cost matrices.
related_works:
- >-
  RouteLLM / OmniRouter: Centralized router for model selection; our work provides a decentralized quorum-sensing mechanism
  with multi-seed Pareto validation, explicit agent cost matrices, and stability bounds.
- >-
  Multi-Agent Debate / Mixture-of-Agents: Fixed rounds or layer aggregation; our work adapts biological quorum sensing with
  quorum quenching and empirical robustness checks across heterogeneous agents with defined capability/cost pairings.
- >-
  Hierarchical / Reflexive Agent Baselines: Token-matched hierarchical and reflexive architectures; our work outperforms them
  via density-dependent phase transitions, rigorous multi-seed uncertainty entropy quantification, and prompt perturbation
  robustness.
inspiration: >-
  Adapted from bacterial quorum sensing (LuxR/LuxI gene regulation circuits in Vibrio fischeri) with quorum quenching, enhanced
  with multi-seed empirical validation, stability bounds under prompt variance, explicit agent capability/cost matrices, and
  hierarchical baseline comparison.
terms:
- term: Quorum Sensing
  definition: >-
    A decentralized coordination mechanism where agents adjust behaviors based on collective density through signal accumulation
    in a shared environment.
- term: Autoinducer
  definition: >-
    A signaling molecule produced by agents proportional to task uncertainty and message weight that accumulates in the shared
    buffer.
- term: Quorum Quenching
  definition: >-
    A degradation and damping term in the autoinducer recurrence relation that prevents runaway positive feedback cascades
    under high message frequency.
- term: Model Escalation
  definition: >-
    Dynamically shifting a task from a cheap lightweight model (e.g., Llama-3-8B) to an expensive reasoning model (e.g., Claude-3.5-Sonnet)
    when collective or local thresholds are crossed.
- term: Capability/Cost Matrix
  definition: >-
    A formal specification mapping heterogeneous agent tiers to their respective per-token monetary costs and reasoning performance
    benchmarks.
summary: >-
  We refine stabilized quorum-sensing multi-agent reasoning by incorporating concrete prompt paraphrase perturbation sets
  and explicit heterogeneous agent capability/cost matrices, achieving robust Pareto efficiency across reasoning benchmarks.
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 4 research artifacts across all iterations.

--- Item 1 ---
id: art_vxt31vyLKAXT
type: dataset
title: Reasoning Benchmarks with Prompt Paraphrases
summary: >-
  Prepared standardized GSM8K (grade school math) and MBPP (Python coding) reasoning benchmarks augmented with systematic
  K=3 prompt paraphrase variants (featuring synonym substitution dictionaries, conditional framing templates, and step-by-step
  interrogative rephrasings) designed specifically for robust multi-agent LLM system evaluation against prompt variance and
  semantic perturbation. Each dataset record has been rigorously standardized into a unified JSON schema grouped by dataset
  name, ensuring separate individual data rows as independent examples containing required 'input' and 'output' fields, accompanied
  by comprehensive flat metadata attributes including fold assignments, row indices, difficulty levels, task categories, and
  all generated paraphrase variants. The pipeline successfully validated schema compliance against exp_sel_data_out expectations
  using the aii-json validation toolkit and automatically generated full, mini, and preview variants for efficient downstream
  consumption, development testing, and qualitative inspection without performance degradation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_mKLUOw5FAqBz
type: research
title: Hierarchical and Reflexive Agent Specifications
summary: >-
  This research artifact provides comprehensive documentation of token-matched hierarchical supervisor-worker architectures,
  reflexive multi-agent workflows, heterogeneous capability and cost matrices for Llama-3-8B and Claude-3.5-Sonnet models,
  and rigorous time-series forecasting baseline comparisons. Specifically, it details how supervisor-worker topologies delegate
  complex task decomposition and verification to high-capability reasoning models while assigning execution to lightweight
  models under strict token-matching protocols. Furthermore, it establishes exact per-token cost and latency matrices, analyzes
  verbal reinforcement learning reflection loops, and empirically evaluates 3-point moving average versus naive last-value
  forecasting baselines across synthetic oscillatory, random walk, and linear trend series.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_Qq4Y04xCvsAw
type: experiment
title: Quorum-Sensing Multi-Agent Reasoning Pareto Analysis
summary: >-
  We introduce and evaluate Quorum-Sensing Autoinduction Recurrence Routing (QS-ARR), a novel decentralized multi-agent LLM
  reasoning architecture that combines discrete-time autoinduction buffer dynamics, non-linear quorum quenching damping (Q
  = gamma * A^2), and task uncertainty entropy to dynamically route reasoning workloads between lightweight models (e.g.,
  Llama-3-8b) and high-capability models (e.g., Claude-3-5-sonnet). Using a comprehensive reasoning benchmark dataset with
  prompt paraphrase perturbations, we simulate multi-agent execution across multiple random seeds against 6 matched-compute
  baselines (static llama, static sonnet, centralized router, independent threshold, reflexive baseline, and hierarchical
  baseline). Our empirical analysis measures accuracy, token cost, latency, and escalation rates, establishing the Pareto
  efficiency frontier of decentralized quorum routing. All experiments, baseline comparisons, and statistical aggregations
  are fully reproducible, accompanied by complete output artifacts (full, mini, preview JSON datasets) and visualization plots.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_5wP95LorUCfy
type: evaluation
title: Stabilized Quorum-Sensing Pareto Evaluation
summary: >-
  Comprehensive multi-seed evaluation of stabilized quorum-sensing multi-agent reasoning. Evaluates token-matched Pareto efficiency
  across 5 random seeds comparing Quorum-Sensing against static Llama-3-8B, static Claude-3.5-Sonnet, centralized router,
  independent threshold, reflexive baseline, and hierarchical supervisor-worker baseline. Measures accuracy vs. token cost
  and monetary expenditure using capability/cost matrices. Analyzes message frequency spike stability under synthetic Poisson
  message arrival surges and stress spikes, tracking autoinducer recurrence values and escalation cascading rates. Quantifies
  epistemic uncertainty via multi-sample generation variance and message token weighting. Evaluates prompt perturbation robustness
  across concrete prompt paraphrase sets. Performs quorum-quenching ablation analyses measuring accuracy and runaway escalation
  deltas when disabling degradation damping or varying damping coefficients. Outputs full, mini, and preview JSON evaluation
  results adhering to schema, along with publication-quality vector PDF and PNG figures for Pareto efficiency, spike stability,
  and quorum ablation failure modes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 4 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
title: Reasoning Benchmarks with Prompt Paraphrases
summary: >-
  Prepared standardized GSM8K (grade school math) and MBPP (Python coding) reasoning benchmarks augmented with systematic
  K=3 prompt paraphrase variants (featuring synonym substitution dictionaries, conditional framing templates, and step-by-step
  interrogative rephrasings) designed specifically for robust multi-agent LLM system evaluation against prompt variance and
  semantic perturbation. Each dataset record has been rigorously standardized into a unified JSON schema grouped by dataset
  name, ensuring separate individual data rows as independent examples containing required 'input' and 'output' fields, accompanied
  by comprehensive flat metadata attributes including fold assignments, row indices, difficulty levels, task categories, and
  all generated paraphrase variants. The pipeline successfully validated schema compliance against exp_sel_data_out expectations
  using the aii-json validation toolkit and automatically generated full, mini, and preview variants for efficient downstream
  consumption, development testing, and qualitative inspection without performance degradation.
id: art_vxt31vyLKAXT

type: research
title: Hierarchical and Reflexive Agent Specifications
summary: >-
  This research artifact provides comprehensive documentation of token-matched hierarchical supervisor-worker architectures,
  reflexive multi-agent workflows, heterogeneous capability and cost matrices for Llama-3-8B and Claude-3.5-Sonnet models,
  and rigorous time-series forecasting baseline comparisons. Specifically, it details how supervisor-worker topologies delegate
  complex task decomposition and verification to high-capability reasoning models while assigning execution to lightweight
  models under strict token-matching protocols. Furthermore, it establishes exact per-token cost and latency matrices, analyzes
  verbal reinforcement learning reflection loops, and empirically evaluates 3-point moving average versus naive last-value
  forecasting baselines across synthetic oscillatory, random walk, and linear trend series.
id: art_mKLUOw5FAqBz

type: experiment
title: Quorum-Sensing Multi-Agent Reasoning Pareto Analysis
summary: >-
  We introduce and evaluate Quorum-Sensing Autoinduction Recurrence Routing (QS-ARR), a novel decentralized multi-agent LLM
  reasoning architecture that combines discrete-time autoinduction buffer dynamics, non-linear quorum quenching damping (Q
  = gamma * A^2), and task uncertainty entropy to dynamically route reasoning workloads between lightweight models (e.g.,
  Llama-3-8b) and high-capability models (e.g., Claude-3-5-sonnet). Using a comprehensive reasoning benchmark dataset with
  prompt paraphrase perturbations, we simulate multi-agent execution across multiple random seeds against 6 matched-compute
  baselines (static llama, static sonnet, centralized router, independent threshold, reflexive baseline, and hierarchical
  baseline). Our empirical analysis measures accuracy, token cost, latency, and escalation rates, establishing the Pareto
  efficiency frontier of decentralized quorum routing. All experiments, baseline comparisons, and statistical aggregations
  are fully reproducible, accompanied by complete output artifacts (full, mini, preview JSON datasets) and visualization plots.
id: art_Qq4Y04xCvsAw

type: evaluation
title: Stabilized Quorum-Sensing Pareto Evaluation
summary: >-
  Comprehensive multi-seed evaluation of stabilized quorum-sensing multi-agent reasoning. Evaluates token-matched Pareto efficiency
  across 5 random seeds comparing Quorum-Sensing against static Llama-3-8B, static Claude-3.5-Sonnet, centralized router,
  independent threshold, reflexive baseline, and hierarchical supervisor-worker baseline. Measures accuracy vs. token cost
  and monetary expenditure using capability/cost matrices. Analyzes message frequency spike stability under synthetic Poisson
  message arrival surges and stress spikes, tracking autoinducer recurrence values and escalation cascading rates. Quantifies
  epistemic uncertainty via multi-sample generation variance and message token weighting. Evaluates prompt perturbation robustness
  across concrete prompt paraphrase sets. Performs quorum-quenching ablation analyses measuring accuracy and runaway escalation
  deltas when disabling degradation damping or varying damping coefficients. Outputs full, mini, and preview JSON evaluation
  results adhering to schema, along with publication-quality vector PDF and PNG figures for Pareto efficiency, spike stability,
  and quorum ablation failure modes.
id: art_5wP95LorUCfy
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

This is the FIRST paper draft. Write a complete research paper from scratch based on the hypothesis and all available artifacts.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-01 15:14:30 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [3] SYSTEM-USER prompt · 2026-08-01 15:16:41 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most r
  - [agent_human_user_prompt]: Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
</available_domain_handbooks>
<hypothesis>
The research hypothesis.

kind: hypothesis
title: Stabilized Quorum-Sensing Multi-Agent Reasoning
hypothesis: >-
  Governing decentralized multi-agent LLM model escalation through discrete-time autoinduction recurrence relations with degradation
  damping (quorum quenching), self-consistency entropy uncertainty signals, concrete prompt paraphrase sets (synonym substitution
  and structural rephrasing), explicit capability/cost matrices for heterogeneous agent pairs (e.g., Llama-3-8B base vs. Claude-3.5-Sonnet
  reasoner), multi-seed empirical validation, stability verification, and token-matched hierarchical and reflexive baselines
  optimizes Pareto efficiency across diverse reasoning benchmark classes without runaway escalation cascades.
motivation: >-
  Multi-agent LLM systems struggle with token expenditure spikes and variance from self-consistency sample noise and prompt
  phrasing. Addressing reviewer feedback by specifying concrete prompt paraphrase methods and explicit capability/cost matrices
  for heterogeneous agents establishes robust reproducibility and true Pareto dominance under extreme message frequency spikes.
assumptions:
- >-
  Multi-seed evaluations across random seeds yield reliable mean and variance estimates for Pareto efficiency curves of accuracy
  versus token expenditure.
- >-
  Theoretical stability bounds for degradation damping (quorum quenching) remain robust under heavy prompt-length variance
  and heterogeneous agent capabilities.
- >-
  Token-matched hierarchical and reflexive baselines provide rigorous comparative standards for evaluating collective density-dependent
  phase transitions.
- >-
  Self-consistency entropy across multi-sample generation scores, combined with message token weighting and explicit agent
  cost matrices, accurately captures epistemic uncertainty.
investigation_approach: >-
  Implement multi-agent simulations across diverse reasoning benchmark classes (math and code generation) with multi-seed
  runs reporting mean and variance. Test degradation rates, Hill coefficients, and explicit agent heterogeneity (pairing Llama-3-8B
  base models with Claude-3.5-Sonnet advanced reasoners under defined capability/cost matrices) across prompt paraphrase sets
  (synonym substitution and structural rephrasing). Benchmark against static routing, centralized routers, decentralized independent
  thresholds, and recent token-matched hierarchical and reflexive baselines, incorporating strict token-matched context accounting
  and conceptual architecture specifications.
success_criteria: >-
  Stabilized quorum-sensing routing achieves statistically significant Pareto efficiency gains (mean and variance across random
  seeds) over static, centralized, independent, hierarchical, and reflexive baselines, maintaining proven stability under
  extreme message frequency spikes and heavy prompt variance with explicit perturbation sets and cost matrices.
related_works:
- >-
  RouteLLM / OmniRouter: Centralized router for model selection; our work provides a decentralized quorum-sensing mechanism
  with multi-seed Pareto validation, explicit agent cost matrices, and stability bounds.
- >-
  Multi-Agent Debate / Mixture-of-Agents: Fixed rounds or layer aggregation; our work adapts biological quorum sensing with
  quorum quenching and empirical robustness checks across heterogeneous agents with defined capability/cost pairings.
- >-
  Hierarchical / Reflexive Agent Baselines: Token-matched hierarchical and reflexive architectures; our work outperforms them
  via density-dependent phase transitions, rigorous multi-seed uncertainty entropy quantification, and prompt perturbation
  robustness.
inspiration: >-
  Adapted from bacterial quorum sensing (LuxR/LuxI gene regulation circuits in Vibrio fischeri) with quorum quenching, enhanced
  with multi-seed empirical validation, stability bounds under prompt variance, explicit agent capability/cost matrices, and
  hierarchical baseline comparison.
terms:
- term: Quorum Sensing
  definition: >-
    A decentralized coordination mechanism where agents adjust behaviors based on collective density through signal accumulation
    in a shared environment.
- term: Autoinducer
  definition: >-
    A signaling molecule produced by agents proportional to task uncertainty and message weight that accumulates in the shared
    buffer.
- term: Quorum Quenching
  definition: >-
    A degradation and damping term in the autoinducer recurrence relation that prevents runaway positive feedback cascades
    under high message frequency.
- term: Model Escalation
  definition: >-
    Dynamically shifting a task from a cheap lightweight model (e.g., Llama-3-8B) to an expensive reasoning model (e.g., Claude-3.5-Sonnet)
    when collective or local thresholds are crossed.
- term: Capability/Cost Matrix
  definition: >-
    A formal specification mapping heterogeneous agent tiers to their respective per-token monetary costs and reasoning performance
    benchmarks.
summary: >-
  We refine stabilized quorum-sensing multi-agent reasoning by incorporating concrete prompt paraphrase perturbation sets
  and explicit heterogeneous agent capability/cost matrices, achieving robust Pareto efficiency across reasoning benchmarks.
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 4 research artifacts across all iterations.

--- Item 1 ---
id: art_vxt31vyLKAXT
type: dataset
title: Reasoning Benchmarks with Prompt Paraphrases
summary: >-
  Prepared standardized GSM8K (grade school math) and MBPP (Python coding) reasoning benchmarks augmented with systematic
  K=3 prompt paraphrase variants (featuring synonym substitution dictionaries, conditional framing templates, and step-by-step
  interrogative rephrasings) designed specifically for robust multi-agent LLM system evaluation against prompt variance and
  semantic perturbation. Each dataset record has been rigorously standardized into a unified JSON schema grouped by dataset
  name, ensuring separate individual data rows as independent examples containing required 'input' and 'output' fields, accompanied
  by comprehensive flat metadata attributes including fold assignments, row indices, difficulty levels, task categories, and
  all generated paraphrase variants. The pipeline successfully validated schema compliance against exp_sel_data_out expectations
  using the aii-json validation toolkit and automatically generated full, mini, and preview variants for efficient downstream
  consumption, development testing, and qualitative inspection without performance degradation.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 2 ---
id: art_mKLUOw5FAqBz
type: research
title: Hierarchical and Reflexive Agent Specifications
summary: >-
  This research artifact provides comprehensive documentation of token-matched hierarchical supervisor-worker architectures,
  reflexive multi-agent workflows, heterogeneous capability and cost matrices for Llama-3-8B and Claude-3.5-Sonnet models,
  and rigorous time-series forecasting baseline comparisons. Specifically, it details how supervisor-worker topologies delegate
  complex task decomposition and verification to high-capability reasoning models while assigning execution to lightweight
  models under strict token-matching protocols. Furthermore, it establishes exact per-token cost and latency matrices, analyzes
  verbal reinforcement learning reflection loops, and empirically evaluates 3-point moving average versus naive last-value
  forecasting baselines across synthetic oscillatory, random walk, and linear trend series.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 3 ---
id: art_Qq4Y04xCvsAw
type: experiment
title: Quorum-Sensing Multi-Agent Reasoning Pareto Analysis
summary: >-
  We introduce and evaluate Quorum-Sensing Autoinduction Recurrence Routing (QS-ARR), a novel decentralized multi-agent LLM
  reasoning architecture that combines discrete-time autoinduction buffer dynamics, non-linear quorum quenching damping (Q
  = gamma * A^2), and task uncertainty entropy to dynamically route reasoning workloads between lightweight models (e.g.,
  Llama-3-8b) and high-capability models (e.g., Claude-3-5-sonnet). Using a comprehensive reasoning benchmark dataset with
  prompt paraphrase perturbations, we simulate multi-agent execution across multiple random seeds against 6 matched-compute
  baselines (static llama, static sonnet, centralized router, independent threshold, reflexive baseline, and hierarchical
  baseline). Our empirical analysis measures accuracy, token cost, latency, and escalation rates, establishing the Pareto
  efficiency frontier of decentralized quorum routing. All experiments, baseline comparisons, and statistical aggregations
  are fully reproducible, accompanied by complete output artifacts (full, mini, preview JSON datasets) and visualization plots.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_5wP95LorUCfy
type: evaluation
title: Stabilized Quorum-Sensing Pareto Evaluation
summary: >-
  Comprehensive multi-seed evaluation of stabilized quorum-sensing multi-agent reasoning. Evaluates token-matched Pareto efficiency
  across 5 random seeds comparing Quorum-Sensing against static Llama-3-8B, static Claude-3.5-Sonnet, centralized router,
  independent threshold, reflexive baseline, and hierarchical supervisor-worker baseline. Measures accuracy vs. token cost
  and monetary expenditure using capability/cost matrices. Analyzes message frequency spike stability under synthetic Poisson
  message arrival surges and stress spikes, tracking autoinducer recurrence values and escalation cascading rates. Quantifies
  epistemic uncertainty via multi-sample generation variance and message token weighting. Evaluates prompt perturbation robustness
  across concrete prompt paraphrase sets. Performs quorum-quenching ablation analyses measuring accuracy and runaway escalation
  deltas when disabling degradation damping or varying damping coefficients. Outputs full, mini, and preview JSON evaluation
  results adhering to schema, along with publication-quality vector PDF and PNG figures for Pareto efficiency, spike stability,
  and quorum ablation failure modes.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 4 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

type: dataset
title: Reasoning Benchmarks with Prompt Paraphrases
summary: >-
  Prepared standardized GSM8K (grade school math) and MBPP (Python coding) reasoning benchmarks augmented with systematic
  K=3 prompt paraphrase variants (featuring synonym substitution dictionaries, conditional framing templates, and step-by-step
  interrogative rephrasings) designed specifically for robust multi-agent LLM system evaluation against prompt variance and
  semantic perturbation. Each dataset record has been rigorously standardized into a unified JSON schema grouped by dataset
  name, ensuring separate individual data rows as independent examples containing required 'input' and 'output' fields, accompanied
  by comprehensive flat metadata attributes including fold assignments, row indices, difficulty levels, task categories, and
  all generated paraphrase variants. The pipeline successfully validated schema compliance against exp_sel_data_out expectations
  using the aii-json validation toolkit and automatically generated full, mini, and preview variants for efficient downstream
  consumption, development testing, and qualitative inspection without performance degradation.
id: art_vxt31vyLKAXT

type: research
title: Hierarchical and Reflexive Agent Specifications
summary: >-
  This research artifact provides comprehensive documentation of token-matched hierarchical supervisor-worker architectures,
  reflexive multi-agent workflows, heterogeneous capability and cost matrices for Llama-3-8B and Claude-3.5-Sonnet models,
  and rigorous time-series forecasting baseline comparisons. Specifically, it details how supervisor-worker topologies delegate
  complex task decomposition and verification to high-capability reasoning models while assigning execution to lightweight
  models under strict token-matching protocols. Furthermore, it establishes exact per-token cost and latency matrices, analyzes
  verbal reinforcement learning reflection loops, and empirically evaluates 3-point moving average versus naive last-value
  forecasting baselines across synthetic oscillatory, random walk, and linear trend series.
id: art_mKLUOw5FAqBz

type: experiment
title: Quorum-Sensing Multi-Agent Reasoning Pareto Analysis
summary: >-
  We introduce and evaluate Quorum-Sensing Autoinduction Recurrence Routing (QS-ARR), a novel decentralized multi-agent LLM
  reasoning architecture that combines discrete-time autoinduction buffer dynamics, non-linear quorum quenching damping (Q
  = gamma * A^2), and task uncertainty entropy to dynamically route reasoning workloads between lightweight models (e.g.,
  Llama-3-8b) and high-capability models (e.g., Claude-3-5-sonnet). Using a comprehensive reasoning benchmark dataset with
  prompt paraphrase perturbations, we simulate multi-agent execution across multiple random seeds against 6 matched-compute
  baselines (static llama, static sonnet, centralized router, independent threshold, reflexive baseline, and hierarchical
  baseline). Our empirical analysis measures accuracy, token cost, latency, and escalation rates, establishing the Pareto
  efficiency frontier of decentralized quorum routing. All experiments, baseline comparisons, and statistical aggregations
  are fully reproducible, accompanied by complete output artifacts (full, mini, preview JSON datasets) and visualization plots.
id: art_Qq4Y04xCvsAw

type: evaluation
title: Stabilized Quorum-Sensing Pareto Evaluation
summary: >-
  Comprehensive multi-seed evaluation of stabilized quorum-sensing multi-agent reasoning. Evaluates token-matched Pareto efficiency
  across 5 random seeds comparing Quorum-Sensing against static Llama-3-8B, static Claude-3.5-Sonnet, centralized router,
  independent threshold, reflexive baseline, and hierarchical supervisor-worker baseline. Measures accuracy vs. token cost
  and monetary expenditure using capability/cost matrices. Analyzes message frequency spike stability under synthetic Poisson
  message arrival surges and stress spikes, tracking autoinducer recurrence values and escalation cascading rates. Quantifies
  epistemic uncertainty via multi-sample generation variance and message token weighting. Evaluates prompt perturbation robustness
  across concrete prompt paraphrase sets. Performs quorum-quenching ablation analyses measuring accuracy and runaway escalation
  deltas when disabling degradation damping or varying damping coefficients. Outputs full, mini, and preview JSON evaluation
  results adhering to schema, along with publication-quality vector PDF and PNG figures for Pareto efficiency, spike stability,
  and quorum ablation failure modes.
id: art_5wP95LorUCfy
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

This is the FIRST paper draft. Write a complete research paper from scratch based on the hypothesis and all available artifacts.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Your ONLY output is the structured JSON.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_om2tRiXGCTOe/3_invention_loop/iter_1/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-01 15:16:41 UTC

```
Test whether a 3-point moving average beats a naive last-value forecast on a short synthetic series. Keep the investigation minimal.
```

### [5] SKILL-INPUT — aii-paper-writing · 2026-08-01 15:16:47 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: Academic paper writing guidance for AI research. Covers paper structure, figure placeholders, bibliography building with Semantic Scholar, and citation rules. Does NOT cover LaTeX compilation or figure file generation — see aii-paper-to-latex for that.
---

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [6] SKILL-INPUT — aii-semscholar-bib · 2026-08-01 15:16:47 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
