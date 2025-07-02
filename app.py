import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

# --- SETUP ---
st.set_page_config(page_title="Fitness Nutrition AI", layout="wide", page_icon="🍏")
st.title("🍏 Fitness Nutrition AI Assistant")
st.markdown("*Your personalized nutrition and fitness companion*")

# --- SIDEBAR (User Input) ---
with st.sidebar:
    st.header("⚙️ Your Preferences")
    
    # Personal Information
    st.subheader("Personal Info")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.slider("Age", 18, 80, 30)
    weight = st.number_input("Weight (kg)", 40.0, 200.0, 70.0, step=0.5)
    height = st.number_input("Height (cm)", 140, 220, 175)
    
    # Activity and Goals
    st.subheader("Activity & Goals")
    activity_level = st.selectbox("Activity Level", 
                                ["Sedentary", "Light", "Moderate", "Active", "Very Active"])
    diet_type = st.selectbox("Diet Type", 
                           ["Balanced", "Keto", "Vegan", "Low-Carb", "High-Protein", "Mediterranean"])
    goal = st.selectbox("Goal", ["Lose Weight", "Maintain Weight", "Gain Muscle", "Improve Health"])
    
    # Health Conditions (Optional)
    st.subheader("Health Info (Optional)")
    allergies = st.text_input("Food Allergies/Restrictions", placeholder="e.g., nuts, dairy, gluten")
    medical_conditions = st.text_input("Medical Conditions", placeholder="e.g., diabetes, hypertension")

# --- CALORIE CALCULATOR (Harris-Benedict Formula) ---
def calculate_calories(weight, height, age, gender, activity_level, goal):
    # BMR Calculation - Different formulas for men and women
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # Female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    # Activity Multiplier
    activity_mult = {
        "Sedentary": 1.2,
        "Light": 1.375,
        "Moderate": 1.55,
        "Active": 1.725,
        "Very Active": 1.9
    }[activity_level]
    
    tdee = bmr * activity_mult
    
    # Adjust for goal
    if goal == "Lose Weight":
        return tdee - 500  # 500 calorie deficit for ~1 lb/week loss
    elif goal == "Gain Muscle":
        return tdee + 300  # 300 calorie surplus
    else:
        return tdee

# Calculate calories
calories = calculate_calories(weight, height, age, gender, activity_level, goal)

# --- MAIN DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Daily Calories", f"{int(calories)} kcal")

with col2:
    bmi = weight / ((height/100) ** 2)
    bmi_category = "Normal" if 18.5 <= bmi < 25 else "Underweight" if bmi < 18.5 else "Overweight" if bmi < 30 else "Obese"
    st.metric("BMI", f"{bmi:.1f}", bmi_category)

with col3:
    water_intake = weight * 35  # ml per kg body weight
    st.metric("Water Goal", f"{water_intake:.0f} ml")

# --- MEAL PLANNER ---
st.header("🍽️ Your Daily Meal Plan")

# Macro Split (Customize based on diet)
macro_splits = {
    "Balanced": {"Carbs": 0.5, "Protein": 0.25, "Fat": 0.25},
    "Keto": {"Carbs": 0.05, "Protein": 0.2, "Fat": 0.75},
    "High-Protein": {"Carbs": 0.3, "Protein": 0.4, "Fat": 0.3},
    "Low-Carb": {"Carbs": 0.2, "Protein": 0.35, "Fat": 0.45},
    "Vegan": {"Carbs": 0.55, "Protein": 0.2, "Fat": 0.25},
    "Mediterranean": {"Carbs": 0.45, "Protein": 0.25, "Fat": 0.3}
}

macros = macro_splits.get(diet_type, macro_splits["Balanced"])

st.subheader("📊 Macro Breakdown")
macro_cols = st.columns(3)

for i, (macro, ratio) in enumerate(macros.items()):
    # Calculate grams and calories
    if macro in ['Carbs', 'Protein']:
        grams = (calories * ratio) / 4
        macro_calories = grams * 4
    else:  # Fat
        grams = (calories * ratio) / 9
        macro_calories = grams * 9
    
    with macro_cols[i]:
        st.metric(
            f"{macro} ({int(ratio*100)}%)",
            f"{int(grams)}g",
            f"{int(macro_calories)} kcal"
        )

# Enhanced Meal Plans based on diet type
meal_plans = {
    "Balanced": {
        "Breakfast": "Oatmeal with berries and almonds (350 kcal)",
        "Lunch": "Grilled chicken salad with quinoa (450 kcal)",
        "Dinner": "Salmon with sweet potato and broccoli (500 kcal)",
        "Snacks": "Greek yogurt with nuts (200 kcal)"
    },
    "Keto": {
        "Breakfast": "Scrambled eggs with avocado and bacon (400 kcal)",
        "Lunch": "Caesar salad with grilled chicken, no croutons (350 kcal)",
        "Dinner": "Ribeye steak with buttered asparagus (600 kcal)",
        "Snacks": "Cheese and macadamia nuts (250 kcal)"
    },
    "Vegan": {
        "Breakfast": "Smoothie bowl with banana, spinach, and chia seeds (300 kcal)",
        "Lunch": "Chickpea Buddha bowl with tahini dressing (450 kcal)",
        "Dinner": "Lentil curry with brown rice (500 kcal)",
        "Snacks": "Hummus with vegetables (150 kcal)"
    },
    "High-Protein": {
        "Breakfast": "Protein pancakes with Greek yogurt (400 kcal)",
        "Lunch": "Turkey and quinoa power bowl (500 kcal)",
        "Dinner": "Grilled cod with roasted vegetables (450 kcal)",
        "Snacks": "Protein shake with banana (250 kcal)"
    }
}

st.subheader("🥗 Suggested Meal Plan")
current_meal_plan = meal_plans.get(diet_type, meal_plans["Balanced"])

for meal, desc in current_meal_plan.items():
    st.write(f"**{meal}:** {desc}")

# --- RECIPE SUGGESTER ---
st.header("🔍 Recipe Finder")
col1, col2 = st.columns(2)

with col1:
    meal_type = st.selectbox("Meal Type", ["Breakfast", "Lunch", "Dinner", "Snack", "Any"])

with col2:
    cuisine = st.selectbox("Cuisine", ["Any", "Mediterranean", "Asian", "American", "Mexican", "Italian"])

food_search = st.text_input("Search for recipes", placeholder="e.g., 'high-protein breakfast'")

if food_search:
    st.success(f"🔎 Recipe suggestions for '{food_search}':")
    
    # Mock recipe database - in real app, this would be from an API
    recipes = [
        "🥞 Protein pancakes with banana & almond butter",
        "🥗 Quinoa chickpea power bowl",
        "🐟 Baked salmon with herbs and lemon",
        "🥤 Green smoothie with spinach and mango",
        "🍳 Veggie-packed omelet with feta cheese"
    ]
    
    for recipe in recipes[:3]:  # Show top 3 matches
        st.write(f"- {recipe}")

# --- AI NUTRITION CHAT ---
st.header("💬 Nutrition Q&A")
user_question = st.text_input("Ask a nutrition question", 
                            placeholder="e.g., 'What should I eat before a workout?'")

if user_question:
    # Enhanced responses based on common questions
    responses = {
        "pre-workout": "Eat a balanced snack 1-2 hours before working out. Good options: banana with peanut butter, oatmeal with berries, or Greek yogurt with granola.",
        "post-workout": "Within 30 minutes after workout, have protein and carbs. Try: chocolate milk, protein shake with banana, or chicken with rice.",
        "weight loss": "Focus on a caloric deficit while maintaining protein intake. Eat plenty of vegetables, lean proteins, and whole grains.",
        "muscle gain": "Eat in a slight caloric surplus with adequate protein (0.8-1g per lb body weight). Include resistance training.",
        "hydration": f"Aim for {water_intake:.0f}ml of water daily, more if you're active. Monitor urine color - pale yellow is ideal."
    }
    
    # Simple keyword matching for demo
    response_key = next((key for key in responses.keys() if key in user_question.lower()), None)
    
    if response_key:
        response = responses[response_key]
    else:
        response = "That's a great question! For personalized nutrition advice, consider consulting with a registered dietitian."
    
    st.info(f"**🤖 AI Nutritionist:** {response}")

# --- FOOD LOG TRACKER ---
st.header("📝 Food Diary")

# Create columns for food logging
log_col1, log_col2 = st.columns(2)

with log_col1:
    st.subheader("Add Food Entry")
    food_entry = st.text_input("Food item", placeholder="e.g., '1 cup oatmeal'")
    estimated_calories = st.number_input("Estimated Calories", 0, 2000, 0, step=10)
    
    if st.button("📝 Log Food", type="primary"):
        if food_entry:
            # Create or load food log
            log_file = "food_log.json"
            
            try:
                if os.path.exists(log_file):
                    with open(log_file, "r") as f:
                        food_log = json.load(f)
                else:
                    food_log = []
                
                # Add new entry
                entry = {
                    "timestamp": datetime.now().isoformat(),
                    "food": food_entry,
                    "calories": estimated_calories,
                    "date": datetime.now().strftime("%Y-%m-%d")
                }
                food_log.append(entry)
                
                # Save updated log
                with open(log_file, "w") as f:
                    json.dump(food_log, f, indent=2)
                
                st.success("✅ Food logged successfully!")
                
            except Exception as e:
                st.error(f"Error saving food log: {e}")

with log_col2:
    st.subheader("Today's Summary")
    
    # Load and display today's entries
    log_file = "food_log.json"
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                food_log = json.load(f)
            
            today = datetime.now().strftime("%Y-%m-%d")
            today_entries = [entry for entry in food_log if entry.get("date") == today]
            
            if today_entries:
                total_calories = sum(entry.get("calories", 0) for entry in today_entries)
                st.metric("Calories Consumed", f"{total_calories} kcal", 
                         f"{total_calories - int(calories)} vs goal")
                
                st.write("**Today's Foods:**")
                for entry in today_entries[-5:]:  # Show last 5 entries
                    time_str = datetime.fromisoformat(entry["timestamp"]).strftime("%H:%M")
                    st.write(f"• {time_str}: {entry['food']} ({entry['calories']} kcal)")
            else:
                st.info("No food entries for today yet.")
                
        except Exception as e:
            st.error(f"Error loading food log: {e}")
    else:
        st.info("Start logging food to see your daily summary!")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>🍏 Fitness Nutrition AI Assistant</p>
    <p><small>This app provides general nutrition information and should not replace professional medical advice.</small></p>
</div>
""", unsafe_allow_html=True)
