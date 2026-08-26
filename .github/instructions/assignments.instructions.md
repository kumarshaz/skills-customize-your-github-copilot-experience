---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files should follow the structure and standards below.

## 1. Template Usage

- Follow [`templates/assignment-template.md`](../../templates/assignment-template.md) as the canonical structure.
- Store each assignment as `assignments/<assignment-id>/README.md`.
- Do not remove or skip required sections from the template.
- Keep the existing heading levels and icon prefixes: `# 📘 Assignment`, `## 🎯 Objective`, `## 📝 Tasks`, and `### 🛠️` for each task.

## 2. Section Guidance

The section headers and content should reflect the template:

- **Title**: Replace `[Assignment Title]` with a short, descriptive name.
- **Objective**: Write 1-2 sentences describing what students will learn or build.
- **Tasks**: Give each task a specific, action-oriented title, followed by `#### Description` and `#### Requirements`.
- **Description**: State exactly what the student must do using clear, encouraging language.
- **Requirements**: Begin with `Completed program should:` and list specific, observable outcomes as bullets.
- **Examples**: Use fenced code blocks for input, output, or example usage when they clarify the expected behavior.

## 3. Student-Facing Standards

- Keep terminology appropriate for the assignment's stated skill level.
- Make requirements measurable and avoid vague instructions such as "make it good" or "handle everything."
- Use consistent names for functions, variables, files, and concepts throughout the assignment.
- Do not add sections outside the template unless the assignment explicitly requires them.