import time
# Function to type out text with a delay for better game feel
def type_text(text, delay=0.05):
    """Print text one character at a time with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # To move to the next line after the text is printed

def start_game():
    type_text("🌟 Welcome to *The Almanack of Naval Ravikant: The Journey to Wealth and Happiness* 🌟")
    time.sleep(1)
    type_text(
        "You are about to embark on a journey inspired by Naval Ravikant's wisdom on building wealth, achieving happiness, "
        "and mastering life. Your decisions will determine how well you internalize and apply these timeless principles.")
    time.sleep(1.5)
    print()
    type_text(
        "🧘‍♂️ Remember: True wealth is freedom, and true happiness comes from within. Are you ready to navigate the path?")
    print()
    time.sleep(1.5)
    type_text("\n💼 The journey begins now. Every choice will shape your future... 💼\n")
    play_game()

def play_game():
    score = 0  # Keep track of the player's score based on decisions

    # Question 1: The Definition of Wealth
    type_text("\n💼 Question 1: The Definition of Wealth 💼")
    time.sleep(1.5)
    move1 = input("You’re starting a new business. How do you begin?\n"
                  "A) Create a product you are passionate about and let the market follow.\n"
                  "B) Blend your passion with market needs, testing ideas iteratively.\n"
                  "C) Focus on finding a scalable market first, and then figure out the product.\n"
                  "D) Copy an already successful business model to reduce risk.\n"
                  "Choose A, B, C, or D: ")

    if move1.upper() == 'B':
        score += 1
        time.sleep(1.5)
        type_text("🔑 Great! Blending passion with market needs ensures both personal fulfillment and profitability.\n")
    elif move1.upper() == 'C':
        type_text("⚠️ Focusing purely on market size may lead to burnout if it doesn’t align with your interests.\n")
    elif move1.upper() == 'A':
        type_text("💡 Passion is important, but without market demand, scaling could be difficult.\n")
    else:
        type_text("⚠️ Copying an existing model might not lead to long-term innovation or personal satisfaction.\n")

    # Question 2: Specific Knowledge
    type_text("\n📚 Question 2: Specific Knowledge 📚")
    time.sleep(1.5)
    move2 = input("You want to develop expertise in your field. How do you approach learning?\n"
                  "A) Focus on hands-on learning and unique experiences that build practical knowledge.\n"
                  "B) Network with experts and learn through mentorship.\n"
                  "C) Follow traditional education paths and certifications to validate your skills.\n"
                  "D) Dive deep into books, podcasts, and online courses, avoiding formal education.\n"
                  "Choose A, B, C, or D: ")

    if move2.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("🎯 Practical, hands-on learning will give you unique skills that stand out.\n")
    elif move2.upper() == 'B':
        type_text("💼 Networking with mentors is a great way to learn from those who’ve walked the path.\n")
    elif move2.upper() == 'C':
        type_text("⚠️ Formal education can validate skills, but practical experience is often more valuable.\n")
    else:
        type_text("📚 Self-learning is excellent but might lack structured growth and feedback from experts.\n")

    # Question 3: Wealth vs. Money
    type_text("\n💰 Question 3: Wealth vs. Money 💰")
    time.sleep(1.5)
    move3 = input("You receive a high-paying job offer but with long hours and no flexibility. What do you do?\n"
                  "A) Take the high-paying job and grind to build wealth fast.\n"
                  "B) Look for a job that offers more freedom and flexibility, even with a lower paycheck.\n"
                  "C) Start a side hustle to complement the high-paying job until you can pursue something better.\n"
                  "D) Negotiate better terms to get a higher salary with more flexibility.\n"
                  "Choose A, B, C, or D: ")

    if move3.upper() == 'D':
        score += 1
        time.sleep(1.5)
        type_text("💡 Negotiating better terms can help you maintain balance while still earning more.\n")
    elif move3.upper() == 'C':
        type_text("📈 Starting a side hustle is a great way to transition into something more flexible later.\n")
    elif move3.upper() == 'B':
        type_text("⚖️ Freedom and flexibility are key to long-term happiness, but it may slow down wealth-building.\n")
    else:
        type_text("⚠️ Grinding in a high-paying job could lead to burnout without fulfillment.\n")

    # Question 4: Compounding
    type_text("\n📈 Question 4: Compounding 📈")
    time.sleep(1.5)
    move4 = input("You want to improve your health. How do you approach it?\n"
                  "A) Overhaul your entire diet and exercise routine to see results quickly.\n"
                  "B) Focus on small, incremental improvements, knowing they’ll compound over time.\n"
                  "C) Prioritize one aspect first—either diet or exercise—and build from there.\n"
                  "D) Join a program or hire a coach to accelerate your results.\n"
                  "Choose A, B, C, or D: ")

    if move4.upper() == 'B':
        score += 1
        time.sleep(1.5)
        type_text("💪 Small, consistent improvements compound into major gains over time.\n")
    elif move4.upper() == 'C':
        type_text("📊 Focusing on one aspect at a time can help you avoid overwhelming yourself.\n")
    elif move4.upper() == 'D':
        type_text("🏋️‍♂️ Hiring a coach or joining a program is a great way to get guided support.\n")
    else:
        type_text("⚠️ Trying to overhaul everything at once can lead to burnout.\n")

    # Question 5: Leverage
    type_text("\n⚙️ Question 5: Leverage ⚙️")
    time.sleep(2)
    move5 = input("You have a business idea. How do you scale it?\n"
                  "A) Hire a team to help you execute your vision as quickly as possible.\n"
                  "B) Use technology and automation to scale without needing a large team.\n"
                  "C) Partner with investors to gain capital and scale faster.\n"
                  "D) Bootstrap the business and grow slowly, keeping full ownership.\n"
                  "Choose A, B, C, or D: ")

    if move5.upper() == 'B':
        score += 1
        time.sleep(1.5)
        type_text("🤖 Leveraging technology and automation is a powerful way to scale efficiently.\n")
    elif move5.upper() == 'A':
        type_text("👥 Hiring a team can accelerate execution but requires careful management.\n")
    elif move5.upper() == 'C':
        type_text("💸 Partnering with investors can bring rapid growth but may require giving up control.\n")
    else:
        type_text("🏗 Bootstrapping allows you to keep ownership, but growth may take longer.\n")

    # Question 6: Happiness Is a Choice
    type_text("\n🧘‍♂️ Question 6: Happiness Is a Choice 🧘‍♂️")
    time.sleep(1.5)
    move6 = input("You find yourself stressed at work and feeling unhappy. What do you do?\n"
                  "A) Quit your job and pursue something more meaningful to you.\n"
                  "B) Start exploring side projects to find a new passion while keeping your job.\n"
                  "C) Work on changing your mindset and practicing gratitude.\n"
                  "D) Take a vacation or break to recharge and reassess.\n"
                  "Choose A, B, C, or D: ")

    if move6.upper() == 'C':
        score += 1
        time.sleep(1.5)
        type_text("🌿 Changing your mindset can lead to lasting happiness, regardless of external circumstances.\n")
    elif move6.upper() == 'B':
        type_text("🎨 Exploring side projects can lead to new opportunities while maintaining stability.\n")
    elif move6.upper() == 'D':
        type_text("🛫 Taking a break can provide temporary relief but may not address the root cause.\n")
    else:
        type_text("⚠️ Quitting is a bold move but could leave you financially unstable.\n")

    # Question 7: Judgment Over Time
    type_text("\n⚖️ Question 7: Judgment Over Time ⚖️")
    time.sleep(1.5)
    move7 = input("You have a big decision to make in your career. How do you approach it?\n"
                  "A) Take time to gather more information and reflect before deciding.\n"
                  "B) Trust your gut and make a quick decision, relying on your instincts.\n"
                  "C) Seek advice from mentors and experts before deciding.\n"
                  "D) Avoid making a decision until you feel more confident in your options.\n"
                  "Choose A, B, C, or D: ")

    if move7.upper() == 'A':
        score += 1
        time.sleep(1.5)
        type_text("🕰 Taking time to gather information and reflect improves decision-making over the long term.\n")
    elif move7.upper() == 'C':
        type_text("👥 Seeking advice from others can give you more perspectives, but the final decision rests with you.\n")
    elif move7.upper() == 'B':
        type_text("💡 Quick decisions based on gut instinct can be effective, but they carry risks.\n")
    else:
        type_text("⚠️ Avoiding decisions might delay progress and keep you in a state of indecision.\n")

    # Question 8: Long-Term Thinking
    type_text("\n🔮 Question 8: Long-Term Thinking 🔮")
    time.sleep(1.5)
    move8 = input(
        "You have an opportunity to make a quick profit, but at the cost of sacrificing long-term growth. What do you do?\n"
        "A) Walk away from the opportunity altogether, focusing only on long-term success.\n"
        "B) Take the quick profit while you can and figure out long-term growth later.\n"
        "C) Invest in long-term growth and sacrifice the short-term gain.\n"
        "D) Find a way to balance both—taking some profit while investing for the future.\n"
        "Choose A, B, C, or D: ")

    if move8.upper() == 'D':
        score += 1
        time.sleep(1.5)
        type_text("⚖️ Balancing short-term profit and long-term growth can offer both stability and potential.\n")
    elif move8.upper() == 'C':
        type_text("🌱 Focusing on long-term growth sets you up for lasting success.\n")
    elif move8.upper() == 'A':
        type_text("🔗 Walking away from quick profits can help maintain long-term focus but may miss opportunities.\n")
    else:
        type_text("💸 Taking a quick profit is tempting, but it may not be sustainable.\n")

    # Question 9: Inner Peace
    type_text("\n🧘‍♂️ Question 9: Inner Peace 🧘‍♂️")
    time.sleep(2)
    move9 = input("You’ve achieved financial success but still feel unfulfilled. How do you find peace?\n"
                  "A) Focus on external goals, like earning more money, and hope fulfillment follows.\n"
                  "B) Work on mindfulness and meditation practices to find inner peace.\n"
                  "C) Seek out deeper relationships with friends and family for connection.\n"
                  "D) Pursue hobbies or interests outside of work to diversify your life.\n"
                  "Choose A, B, C, or D: ")

    if move9.upper() == 'B':
        score += 1
        time.sleep(1.5)
        type_text("🧘‍♀️ Focusing on inner peace through mindfulness can bring lasting fulfillment.\n")
    elif move9.upper() == 'C':
        type_text("👥 Building strong relationships can give you a deeper sense of connection and belonging.\n")
    elif move9.upper() == 'D':
        type_text("🎨 Pursuing outside interests can bring balance and joy to your life.\n")
    else:
        type_text("💼 Chasing more money might bring temporary satisfaction, but it won’t guarantee peace.\n")

    # Question 10: Naval’s Framework for Life (Health, Wealth, and Happiness)
    type_text("\n⚖️ Question 10: Naval’s Framework for Life ⚖️")
    time.sleep(1.5)
    move10 = input("You feel like your life is out of balance. How do you address it?\n"
                   "A) Focus on building wealth first, then address health and happiness later.\n"
                   "B) Balance your efforts across health, wealth, and happiness equally right now.\n"
                   "C) Prioritize health first, knowing that wealth and happiness will follow.\n"
                   "D) Focus on happiness first, as it might make building health and wealth easier.\n"
                   "Choose A, B, C, or D: ")

    if move10.upper() == 'B':
        score += 1
        time.sleep(1.5)
        type_text("⚖️ Balancing health, wealth, and happiness gives you a holistic approach to life.\n")
    elif move10.upper() == 'C':
        type_text("💪 Prioritizing health can lead to improvements in both wealth and happiness.\n")
    elif move10.upper() == 'D':
        type_text("😊 Focusing on happiness can bring fulfillment and make achieving other goals easier.\n")
    else:
        type_text(
            "💼 Building wealth first might delay fulfillment in health and happiness, but could bring financial stability.\n")


# After the last question (question 10), call determine_title(score)
    determine_title(score)

def determine_title(score):
    # Titles based on score
    titles = {
        10: "Naval Disciple",
        9: "Wealth and Happiness Seeker",
        7: "Strategic Thinker",
        5: "Growth Learner",
        3: "Novice Explorer",
        0: "Wanderer"
    }

    # Determine the title based on the score
    title = titles.get(score, "Wanderer")

    # Display the final result and feedback
    type_text(f"\n🎉 Congratulations! You’ve completed the journey with a score of {score}/10. 🎉")
    type_text(f"Your final title is: {title}!")

    # Give feedback based on the title
    feedback = {
        "Naval Disciple": "🏆 You've mastered the wisdom of Naval! You are ready to navigate life with clarity, balance, and deep understanding.",
        "Wealth and Happiness Seeker": "🎯 Great work! You’ve learned how to align wealth-building and happiness, and you're well on your way to living a fulfilled life.",
        "Strategic Thinker": "📈 Good job! You’re developing strong habits of thinking long-term, but there’s still room to deepen your understanding of Naval’s wisdom.",
        "Growth Learner": "⚡ You’re starting to grasp the principles of success and happiness. Keep refining your approach to reach your full potential.",
        "Novice Explorer": "🌱 You’re just beginning your journey into these ideas. Continue learning and apply these principles to see real growth in your life.",
        "Wanderer": "🔰 Your journey has just begun. Take time to reflect on your choices and consider how to improve your understanding of Naval’s philosophies."
    }

    type_text(feedback[title])
    time.sleep(1.5)

    # Bonus video for players who score 7 or higher
    if score >= 7:
        type_text(
            "\n🎥 Bonus! Since you scored 7 or higher, here's a special video to deepen your understanding of Naval’s strategies:")
        type_text("👉 [Bonus Video Link] https://www.youtube.com/watch?v=OqlfWDyS1Io")  # Replace with actual video URL

    # Ask if the player wants to play again
    replay = input("\nWould you like to play again to improve your title? (Yes/No): ").lower()

    if replay == 'yes':
        play_game()  # This will restart the game
    else:
        type_text(
            "Thanks for playing *The Almanack of Naval Ravikant: The Journey to Wealth and Happiness*! Remember, real wealth and happiness come from within. Goodbye!")
start_game()

