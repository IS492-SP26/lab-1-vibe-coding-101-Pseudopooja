## Comparison of Tool A and Tool B

| Criteria | Tool A – VS Code + GitHub Copilot | Tool B – Gemini CLI |
|---------|----------------------------------|---------------------|
| Tool Description | In-editor AI assistant that provides real-time code suggestions and autocompletion while writing Python code. | Command-line based AI tool that generates and edits files directly through the terminal. |
| Game Environment Setup | Copilot suggested pygame setup incrementally, allowing the user to understand and control each step. | Gemini CLI generated the entire game file quickly and handled setup automatically. |
| Player Input Handling | Paddle controls were implemented gradually with Copilot’s inline suggestions, making logic easy to follow. | Player controls were generated correctly in one pass with minimal user intervention. |
| Ball Movement & Collisions | Collision handling worked but was occasionally slightly glitchy, especially during paddle-ball interactions. | Collision handling was smoother and more consistent, with fewer visible gameplay glitches. |
| Score Keeping | Score logic was simple and readable, and easy to tweak during development. | Score tracking was automatically integrated and worked correctly without additional edits. |
| Code Quality | Code was readable and beginner-friendly, with a strong learning focus. | Code was concise and functional, with less emphasis on explanation. |
| Speed of Generation | Slower initially due to incremental generation, but helpful for understanding the logic. | Faster overall since a complete working file was generated quickly. |
| Ease of Use | Very intuitive inside VS Code, especially for editing and making small changes. | Powerful but required comfort with terminal workflows and permission prompts. |
| Debugging & Editing Experience | Copilot was easier to interact with during debugging, as requirements and fixes could be explained naturally through comments and inline prompts within the editor. This made iterative changes more intuitive. | Gemini CLI generated and modified files directly, which was efficient, but offered less conversational guidance during the debugging process. |
| Flexibility & Customization | Highly flexible for iterative changes and experimentation during development. | Flexible for file-level changes but required explicit confirmation for edits. |
| Overall Experience | Felt like a learning-focused tool that supported understanding and gradual development. | Felt like an execution-focused tool optimized for speed and automation. |

## Conclusion & Key Takeaways

This lab demonstrated that generative AI tools influence not only *what* is built, but *how* developers think and work while building it. Key takeaways from this exercise include:

- **Different tools support different stages of development:**  
  VS Code with GitHub Copilot encouraged an exploratory and learning-focused workflow, where requirements could be refined incrementally through comments and inline suggestions. Gemini CLI, on the other hand, excelled at rapid execution by generating complete, working files with minimal setup.

- **Interaction style impacts debugging and understanding:**  
  Copilot’s conversational, in-editor interaction made it easier to explain intent and reason through debugging steps, while Gemini CLI prioritized efficiency by applying changes directly to files with controlled approvals.

- **Speed versus interpretability is a meaningful trade-off:**  
  While Gemini CLI enabled faster transitions from idea to prototype, Copilot provided greater transparency into the underlying logic, which was especially valuable from a learning perspective.

- **Tool choice should be context-driven:**  
  This exercise reinforced that there is no single “best” generative AI tool. Instead, effective use depends on the task, the user’s familiarity with the environment, and whether the goal is rapid implementation or deeper conceptual understanding.

Overall, this assignment helped me recognize my own preferences as a developer and clarified how different generative AI tools can support both my learning process and my productivity in different ways.
