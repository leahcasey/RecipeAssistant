# RecipeAssistant
Slaybake is an interactive recipe-making assistant designed to enhance the usability of online recipes by integrating a Figma app prototype with a Circuit Playground Express. The system helps users follow recipes more efficiently by reducing distractions, eliminating unnecessary scrolling, and providing intuitive feedback.

When using Slaybake, the Figma prototype serves as the main recipe interface, displaying step-by-step instructions in a clear and structured format. Instead of manually scrolling or searching for ingredients, users can navigate hands-free using an ultrasonic sensor embedded in the Circuit Playground. By holding their hand over the sensor for two seconds, users can seamlessly move to the next step without touching their device—preventing interruptions while cooking.

The Circuit Playground Express provides real-time visual feedback using neopixel lights to track progress. At the start, all neopixels are red. As each step is completed, the lights gradually transition to green, giving users a quick visual indication of how much of the recipe they have completed. This ensures users always know their current step without having to check the screen constantly.

Slaybake also includes a built-in timer to help with timed steps in recipes, such as baking or resting dough. Users start the timer by pressing a button on the Circuit Playground, which then triggers the timer interface on the Figma prototype. The neopixels act as a countdown—each light turning off as time progresses. Once the timer completes, users receive a clear indication that they can proceed, helping them stay focused without needing a separate timer app.

To prevent accidental interactions, Slaybake’s ultrasonic sensor is programmed to only respond after a deliberate two-second hold, avoiding unintended step changes. Additionally, the Figma prototype reinforces user actions by synchronizing with the Circuit Playground’s input, ensuring a smooth and integrated experience between the two systems.

Slaybake was evaluated through a user study, where participants interacted with the prototype while thinking aloud, followed by semi-structured interviews. The study revealed that while users found the system engaging and effective, some initial confusion occurred regarding the ultrasonic sensor and switch functionality. Once familiarized, users could easily navigate the prototype and appreciated the hands-free navigation, step tracking, and timer integration. Future improvements include larger labels, clearer prompts, and better onboarding instructions to enhance intuitiveness.

Overall, Slaybake offers an innovative approach to simplifying online recipe navigation, making cooking more accessible, intuitive, and efficient.
