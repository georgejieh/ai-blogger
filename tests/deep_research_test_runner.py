"""Test runner for generating a research draft via Perplexity Deep Research."""

from modules.deep_research import generate_research_draft


def main() -> None:
    """Prompts the user for a freeform input and generates a research draft."""
    user_prompt = input("Enter your full prompt (freeform): ").strip()
    if not user_prompt:
        print("❌ Prompt cannot be empty.")
        return

    print("\n⏳ Generating draft...")
    try:
        content = generate_research_draft(user_prompt)
        print("\n✅ Draft generated successfully. Preview:\n")
        print("=" * 60)
        print("\n".join(content.strip().splitlines()[:10]))
        print("...\n")
        print("📝 Full draft saved to: outputs/articles/")
    except Exception as e:
        print(f"❌ Error generating draft: {e}")


if __name__ == "__main__":
    main()
