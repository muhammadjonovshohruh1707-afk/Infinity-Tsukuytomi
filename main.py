import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.client.session.aiohttp import AiohttpSession

# BAZADAN IMPORT (translations olib tashlandi)
from data import (
    investor_faq,
    investor_faq_categories,
    problems_db, team_db, salary_map, departments, employee_finance
)

TOKEN = "8445838520:AAEybRcF6LNT1rigbJ3TMthzoc3vTwKp_i0"
ADMIN_ID = 1604871776

logging.basicConfig(level=logging.INFO)

# PROXY (PythonAnywhere uchun shart emas)
bot = Bot(token=TOKEN)

dp = Dispatcher()

# --- HOLATLAR ---
class BotStates(StatesGroup):
    waiting_for_search = State()
    waiting_for_auth = State()

# ==========================================================
# 1. START & ASOSIY MENYU
# ==========================================================
@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.clear()

    kb = ReplyKeyboardBuilder()
    kb.button(text="🧠 Major Tree (Tizim)")
    kb.button(text="💼 Investor FAQ")
    kb.button(text="💰 Moliya & Kabinet")
    kb.button(text="🌐 Ijtimoiy Tarmoqlar")
    kb.adjust(2, 2)

    await message.answer(
        "👋 **Infinity Tsukuyomi Boshqaruv Markaziga xush kelibsiz!**\n\n"
        "Kerakli bo'limni tanlang 👇",
        reply_markup=kb.as_markup(resize_keyboard=True),
        parse_mode="Markdown"
    )

# ==========================================================
# 2. MAJOR TREE (MUAMMOLAR & JAMOA)
# ==========================================================
@dp.message(F.text == "🧠 Major Tree (Tizim)")
async def open_major(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="🚨 Muammolar", callback_data="probs_cats")
    builder.button(text="🔍 Qidiruv (AI)", callback_data="probs_search")
    builder.button(text="👥 Jamoa", callback_data="menu_team")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)

    await message.answer("🧠 **Major Tree Tizimi**", reply_markup=builder.as_markup())

# --- MUAMMOLAR ---
@dp.callback_query(F.data == "probs_cats")
async def show_prob_cats(call: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for c_id, db_data in problems_db.items():
        builder.button(text=f"📂 {db_data['name']}", callback_data=f"cat_{c_id}")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)
    await call.message.edit_text("📂 Kategoriya tanlang:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("cat_"))
async def show_problems_list(call: types.CallbackQuery):
    c_id = int(call.data.split("_")[1])
    builder = InlineKeyboardBuilder()
    for p_id, p_data in problems_db[c_id]["problems"].items():
        builder.button(text=f"⚠️ {p_data['title']}", callback_data=f"prob_{c_id}_{p_id}")
    builder.button(text="⬅️ Orqaga", callback_data="probs_cats")
    builder.adjust(1)
    await call.message.edit_text(f"⚠️ **{problems_db[c_id]['name']}**", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("prob_"))
async def show_solutions(call: types.CallbackQuery):
    parts = call.data.split("_")
    c_id, p_id = int(parts[1]), int(parts[2])
    solutions = problems_db[c_id]["problems"][p_id]["solutions"]
    builder = InlineKeyboardBuilder()
    for s_id, s_data in solutions.items():
        builder.button(text=f"🛠 {s_data['desc']}", callback_data=f"sol_{c_id}_{p_id}_{s_id}")
    builder.button(text="⬅️ Orqaga", callback_data=f"cat_{c_id}")
    builder.adjust(1)
    await call.message.edit_text("Yechimni tanlang:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("sol_"))
async def show_scripts(call: types.CallbackQuery):
    parts = call.data.split("_")
    c_id, p_id, s_id = int(parts[1]), int(parts[2]), int(parts[3])
    data = problems_db[c_id]["problems"][p_id]["solutions"][s_id]
    text = f"🛠 **PROTOCOL (#{s_id})**\nAction: {data['desc']}\n\n📜 **Scripts:**\n"
    for script in data['scripts']: text += f"computer:~$ {script}\n"
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Run", callback_data="approve")
    builder.button(text="⬅️ Orqaga", callback_data=f"prob_{c_id}_{p_id}")
    await call.message.edit_text(text, reply_markup=builder.as_markup())

# --- QIDIRUV ---
@dp.callback_query(F.data == "probs_search")
async def start_search(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("🔍 **Muammoni yozing:**")
    await state.set_state(BotStates.waiting_for_search)

@dp.message(BotStates.waiting_for_search)
async def process_search(message: types.Message, state: FSMContext):
    query = message.text.lower()
    results = []
    for c_id, cat_data in problems_db.items():
        for p_id, p_data in cat_data["problems"].items():
            if query in p_data['title'].lower():
                results.append((c_id, p_id, p_data['title']))

    if results:
        builder = InlineKeyboardBuilder()
        for res in results:
            builder.button(text=f"Found: {res[2]}", callback_data=f"prob_{res[0]}_{res[1]}")
        builder.button(text="❌ Yopish", callback_data="close_menu")
        builder.adjust(1)
        await message.answer(f"✅ Natijalar '{query}':", reply_markup=builder.as_markup())
    else:
        await message.answer("❌ Hech narsa topilmadi.")
    await state.set_state(None)

# --- JAMOA ---
@dp.callback_query(F.data == "menu_team")
async def show_departments(call: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for d_id, data_dept in departments.items():
        builder.button(text=data_dept['name'], callback_data=f"dept_{d_id}")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)
    await call.message.edit_text("👥 Jamoa tuzilmasi:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("dept_"))
async def show_dept_roles(call: types.CallbackQuery):
    d_id = call.data.split("_")[1]
    dept_name = departments[d_id]["name"]
    roles = departments[d_id]["roles"]
    builder = InlineKeyboardBuilder()
    for role in roles:
        builder.button(text=f"👤 {role}", callback_data=f"role_{role}_{d_id}")
    builder.button(text="⬅️ Orqaga", callback_data="menu_team")
    builder.adjust(2)
    await call.message.edit_text(f"📂 **{dept_name}**:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("role_"))
async def show_role_details(call: types.CallbackQuery):
    parts = call.data.split("_")
    role, d_id = parts[1], parts[2]
    if role in team_db:
        data = team_db[role]
        text = (f"👤 **{role}**\nIsm: {data['name']}\nStatus: {data['status']}\n\n"
                f"Vazifalar: {', '.join(data['daily'])}")
    else: text = "Ma'lumot topilmadi"
    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data=f"dept_{d_id}")
    await call.message.edit_text(text, reply_markup=builder.as_markup())

# ==========================================================
# 3. INVESTOR FAQ
# ==========================================================
# ==========================================================
# 3. INVESTOR FAQ (YANGILANGAN)
# ==========================================================
@dp.message(F.text == "💼 Investor FAQ")
async def open_faq(message: types.Message):
    builder = InlineKeyboardBuilder()
    # Kategoriyalarni qo'lda yozamiz (chunki bazangizda ID lar bor)
    cats = {
        1: "📈 Moliya ($900M)",
        2: "🛠 Mahsulot va Tech",
        3: "🚀 Marketing va O'sish",
        4: "⚖️ Xatarlar va Qonun",
        5: "🏁 Strategiya va Exit"
    }
    for cat_id, cat_name in cats.items():
        builder.button(text=cat_name, callback_data=f"faqcat_{cat_id}")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)
    await message.answer("💼 **Investorlar uchun FAQ bo'limi**\nKategoriyani tanlang:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("faqcat_"))
async def show_faq_questions(call: types.CallbackQuery):
    cat_id = int(call.data.split("_")[1])
    builder = InlineKeyboardBuilder()

    # Ma'lumotni investor_faq dan filtrlab olamiz
    for q_id, faq_data in investor_faq.items():
        if faq_data.get('cat') == cat_id:
            # Savol matnini qisqartirib tugmaga qo'yamiz
            q_text = faq_data['q']
            builder.button(text=f"❓ {q_text[:35]}...", callback_data=f"faq_{q_id}")

    builder.button(text="⬅️ Orqaga", callback_data="back_faq_cats")
    builder.adjust(1)
    await call.message.edit_text("Savolni tanlang:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("faq_"))
async def show_faq_answer(call: types.CallbackQuery):
    q_id = int(call.data.split("_")[1])
    faq_data = investor_faq[q_id]

    text = f"❓ **SAVOL:**\n{faq_data['q']}\n\n💡 **JAVOB:**\n{faq_data['a']}"

    builder = InlineKeyboardBuilder()
    builder.button(text="⬅️ Orqaga", callback_data=f"faqcat_{faq_data['cat']}")
    await call.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="Markdown")

@dp.callback_query(F.data == "back_faq_cats")
async def back_faq(call: types.CallbackQuery):
    # Asosiy FAQ menyusiga qaytish
    await call.message.delete()
    await open_faq(call.message)

# ==========================================================
# 4. SOCIAL & MOLIYA
# ==========================================================
@dp.message(F.text == "🌐 Ijtimoiy Tarmoqlar")
async def open_social(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📸 Instagram", url="https://www.instagram.com/infinitytsukuyomi.realgame")
    builder.button(text="✈️ Telegram", url="https://t.me/infinitytsukuyomiRealGame")
    builder.button(text="📺 YouTube", url="https://youtube.com/@infinitytsukuyomi.realgame")
    builder.button(text="💼 LinkedIn", url="https://www.linkedin.com/in/shohruh-muhammadjonov-036250348")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)
    await message.answer("🌐 **Bizning ijtimoiy tarmoqlar:**", reply_markup=builder.as_markup())

@dp.message(F.text == "💰 Moliya & Kabinet")
async def open_finance(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📊 Admin Report", callback_data="menu_salary_admin")
    builder.button(text="👤 Shaxsiy kabinet", callback_data="menu_salary_personal")
    builder.button(text="❌ Yopish", callback_data="close_menu")
    builder.adjust(1)
    await message.answer("💰 **Moliya bo'limi**", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "menu_salary_admin")
async def show_salary_admin(call: types.CallbackQuery):
    total = sum(salary_map.values())
    runway = 3_000_000 / (total + 10000)
    text = f"💰 **Admin Report:**\n💵 Total Payroll: ${total:,.0f}\n📅 Runway: {runway:.1f} months"
    await call.message.edit_text(text)

@dp.callback_query(F.data == "menu_salary_personal")
async def auth_step(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text("👤 **Ismingizni kiriting:**")
    await state.set_state(BotStates.waiting_for_auth)

@dp.message(BotStates.waiting_for_auth)
async def personal_cabinet(message: types.Message, state: FSMContext):
    name = message.text.capitalize()
    if name in employee_finance:
        emp_data = employee_finance[name]
        today = datetime.now().day
        text = f"👤 **{name}**\nRol: {emp_data['role']}\nMaosh: ${emp_data['salary']}\n\n"
        text += "✅ To'lov kuni!" if today == 15 else f"⏳ To'lovgacha {abs(15-today)} kun qoldi."
        builder = InlineKeyboardBuilder()
        builder.button(text="✅ OK", callback_data="approve")
        await message.answer(text, reply_markup=builder.as_markup())
    else:
        await message.answer("❌ Xodim topilmadi.")
    await state.set_state(None)

@dp.callback_query(F.data == "close_menu")
async def close_menu(call: types.CallbackQuery):
    await call.message.delete()

@dp.callback_query(F.data == "approve")
async def approve(call: types.CallbackQuery):
    await call.answer("Bajarildi!", show_alert=True)
    await call.message.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())

