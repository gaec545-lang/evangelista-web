# Skill Creator - Create and Optimize Skills

This skill helps create new skills, modify existing skills, measure skill performance, and optimize skill descriptions for better triggering accuracy.

## When to Use This Skill

Use this skill when:
- Creating a new skill from scratch
- Editing or improving an existing skill
- Running evals to test a skill
- Benchmarking skill performance with variance analysis
- Optimizing a skill's description for better triggering

## Core Capabilities

### 1. Creating New Skills

When creating a skill, follow this structure:
```markdown
# Skill Name

Brief description of what this skill does and when to use it.

## When to Use This Skill

Clear triggers for when this skill should be invoked:
- Specific user requests
- Task patterns
- Keywords or phrases

## Core Methodology

Step-by-step approach to accomplish the task:

1. **Step Name**: What to do and why
2. **Step Name**: Next action
3. **Step Name**: Final steps

## Best Practices

- Key principle 1
- Key principle 2
- Key principle 3

## Common Pitfalls to Avoid

- Mistake to avoid
- Another pitfall
- Edge case to watch for

## Examples

### Example 1: [Description]
[Show the expected workflow]

### Example 2: [Description]
[Show another scenario]

## Quality Checks

Before completing, verify:
- [ ] Checklist item 1
- [ ] Checklist item 2
- [ ] Checklist item 3
```

### 2. Skill Description Optimization

Good skill descriptions should:
- **Be specific**: Mention exact triggers and use cases
- **Include keywords**: Terms users might say
- **Be concise**: 2-4 sentences maximum
- **Show value**: What the skill accomplishes
- **List examples**: Common trigger phrases

**Example of a GOOD description:**
```
Use this skill whenever the user wants to create, read, edit, or manipulate Word documents (.docx files). Triggers include: any mention of 'Word doc', 'word document', '.docx', or requests to produce professional documents with formatting like tables of contents, headings, page numbers, or letterheads.
```

**Example of a POOR description:**
```
This skill helps with documents.
```

### 3. Testing Skills with Evals

When testing a skill:

1. **Create test cases** covering:
   - Typical use cases (should trigger)
   - Edge cases (should trigger)
   - Similar but different tasks (should NOT trigger)

2. **Run multiple iterations** (minimum 10) to check variance

3. **Measure**:
   - Trigger accuracy (does it fire when it should?)
   - False positives (does it fire when it shouldn't?)
   - Consistency (same result across runs?)

4. **Document results**:
   - Success rate
   - Common failure patterns
   - Recommended improvements

### 4. Benchmarking Performance

Compare skill performance across iterations:
```
Test Case 1: "Create a presentation about sales data"
- Run 1: ✅ Triggered correctly
- Run 2: ✅ Triggered correctly
- Run 3: ❌ Missed trigger
- Run 4: ✅ Triggered correctly
- Run 5: ✅ Triggered correctly
Success rate: 80%

Test Case 2: "Make slides for my meeting"
- Run 1: ✅ Triggered correctly
- Run 2: ✅ Triggered correctly
- Run 3: ✅ Triggered correctly
- Run 4: ✅ Triggered correctly
- Run 5: ✅ Triggered correctly
Success rate: 100%
```

Analyze variance and identify patterns in failures.

### 5. Iterative Improvement Process

1. **Baseline**: Test current skill version
2. **Identify gaps**: Find where it fails or confuses
3. **Hypothesize**: Why is it failing?
4. **Modify**: Update description or methodology
5. **Re-test**: Run same evals again
6. **Compare**: Did performance improve?
7. **Iterate**: Repeat until optimal

## Skill Quality Principles

### Clarity
- Clear trigger conditions
- Unambiguous scope
- Explicit examples

### Completeness
- Covers main use cases
- Addresses edge cases
- Includes error handling

### Consistency
- Follows template structure
- Uses consistent terminology
- Maintains same style/tone

### Actionability
- Step-by-step instructions
- Concrete examples
- Clear success criteria

## Common Skill Patterns

### Pattern 1: File Format Skills
```markdown
# Skill Name: [Format] Handler

Use when user wants to create, read, or modify [format] files.

Triggers:
- "[format]" mentioned
- File extension like ".[ext]"
- Tasks requiring [format] output

Methodology:
1. Identify the specific task
2. Use appropriate library/tool
3. Apply format-specific best practices
4. Validate output
```

### Pattern 2: Domain Knowledge Skills
```markdown
# Skill Name: [Domain] Expert

Use when user asks about [domain] concepts, implementation, or best practices.

Triggers:
- [Domain] terminology used
- Requests for [domain] guidance
- Implementation questions in [domain]

Methodology:
1. Assess user's knowledge level
2. Provide [domain]-specific context
3. Suggest industry-standard approaches
4. Reference authoritative sources
```

### Pattern 3: Workflow Skills
```markdown
# Skill Name: [Workflow] Automation

Use when user wants to accomplish [specific workflow].

Triggers:
- Keywords: [list key phrases]
- Task descriptions matching [pattern]
- Mentions of [specific tools/outputs]

Methodology:
1. Clarify requirements
2. Break down into steps
3. Execute each step
4. Validate final output
```

## Anti-Patterns to Avoid

❌ **Overly broad scope**: "Use this skill for anything related to data"
✅ **Specific scope**: "Use when creating CSV files with specific column headers and data validation"

❌ **Vague triggers**: "When user needs help"
✅ **Clear triggers**: "When user says 'create a spreadsheet', 'make an Excel file', or mentions .xlsx/.csv"

❌ **No examples**: Just methodology without context
✅ **Rich examples**: Show expected input → process → output

❌ **Missing edge cases**: Only covers happy path
✅ **Comprehensive**: Addresses errors, special cases, alternatives

## Skill Naming Conventions

- **Descriptive**: Name clearly indicates purpose
- **Concise**: 2-4 words maximum
- **Unique**: Distinguishable from other skills
- **Memorable**: Easy to reference

Examples:
- ✅ `docx` (clear, short, memorable)
- ✅ `frontend-design` (specific, descriptive)
- ❌ `helper` (too vague)
- ❌ `the-skill-for-creating-various-document-types` (too long)

## Evaluation Checklist

Before finalizing a skill, verify:

- [ ] Description clearly states when to use it
- [ ] Triggers are specific and testable
- [ ] Methodology is step-by-step
- [ ] Examples cover common scenarios
- [ ] Best practices are included
- [ ] Common pitfalls are documented
- [ ] Quality checks are defined
- [ ] Follows template structure
- [ ] No overlap with existing skills
- [ ] Name follows conventions

## Advanced: Skill Composition

Sometimes multiple skills should work together:

1. **Identify dependencies**: Skill A needs output from Skill B
2. **Define interface**: How do skills communicate?
3. **Test integration**: Do they work together?
4. **Document workflow**: When to use each in sequence

Example:
```
Workflow: Create and email a document
1. Use `docx` skill to create document
2. Use `email` skill to send it
```

## Metadata Best Practices

Include metadata for better organization:
```yaml
skill_name: corporate-website-design
category: web-development
difficulty: intermediate
dependencies: [html, css, javascript]
last_updated: 2026-03-09
version: 1.0
```

## Final Tips

1. **Start simple**: Don't over-engineer on first iteration
2. **Test early**: Run evals before finalizing
3. **Iterate**: Skills improve with use and feedback
4. **Document**: Clear notes help future improvements
5. **Specialize**: Better to have focused skills than one mega-skill

## When NOT to Create a Skill

Don't create a skill if:
- Task is too simple (one-off, no pattern)
- Already covered by existing skill
- Too broad/vague to define clearly
- Rarely needed (less than 1x per month)
- Better handled by general capabilities

Instead, consider:
- Expanding existing skill
- Creating sub-skills
- Documenting as a use case within existing skill