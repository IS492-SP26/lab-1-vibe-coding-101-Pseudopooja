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

This lab helped me realize that generative AI tools affect not just the final output, but also the way I approach problem-solving while building a project. While working on the Ping-Pong game, I noticed a few key differences in how each tool fit into my development process.

Using VS Code with GitHub Copilot felt more exploratory and learning-oriented. I was able to explain my intent through comments, accept or modify suggestions step by step, and gradually refine the code. This made it easier to understand how different parts of the game worked together as I built it.

In contrast, Gemini CLI was much more execution-focused. It generated complete files quickly and handled changes efficiently, which helped me move from an idea to a working version faster. However, this speed sometimes came at the cost of visibility into the logic, especially when compared to Copilot’s in-editor guidance.

Overall, this experience showed me that there is a meaningful trade-off between speed and interpretability. Copilot supported deeper understanding and easier debugging, while Gemini CLI prioritized efficiency and automation. This lab reinforced that there is no single “best” generative AI tool, choosing the right one depends on the task, the stage of development, and whether the goal is learning or rapid implementation.
