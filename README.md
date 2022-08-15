# A Sublime Text command to show your [Clerk](https://github.com/nextjournal/clerk) notebooks

Clerk Sublimed gives you a simple command (`Clerk Sublimed: Show`) to evaluate your Clerk notebooks via Sublime Text. Make sure to bind this command to a keybinding of your choice. (We recommend <kbd>Option</kbd> <kbd>Command</kbd> <kbd>Enter</kbd> on Mac or <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Enter</kbd> for other machines.)

This package requires the [Clojure Sublimed](https://github.com/tonsky/Clojure-Sublimed) package to be installed and active. It also requires an active REPL connection (make sure you ran "Clojure Sublimed: Connect"), otherwise it will fail silently.

## Get started

- Make sure to install the [Clojure Sublimed](https://github.com/tonsky/Clojure-Sublimed) package. Clerk Sublimed only works together with Clojure Sublimed.
- Make sure to connect to your REPL via `Clojure Sublimed: Connect`.
- Open a Clerk notebook and run `Clerk Sublimed: Show` to evaluate the notebook.
- Configure key bindings using `Preferences: Clerk Sublimed Key Bindings`.
