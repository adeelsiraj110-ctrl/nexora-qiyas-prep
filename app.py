"""
Nexora - Qiyas/Aptitude Test Preparation App
Built with Python and Flet Framework
Production-Ready Code for Google Play Store & Apple App Store
"""

import flet as ft
from dataclasses import dataclass
from typing import List, Optional, Callable
from datetime import datetime
import json

# ============================================================================
# DATA MODELS
# ============================================================================

@dataclass
class QuizQuestion:
    """Represents a quiz question with multiple choice options"""
    id: int
    question_ar: str
    question_en: str
    options: List[str]
    correct_answer_index: int
    category: str
    difficulty: str  # Easy, Medium, Hard
    tokens_reward: int = 25


@dataclass
class VideoShort:
    """Represents an educational video short"""
    id: int
    title_ar: str
    title_en: str
    duration: int  # in seconds
    thumbnail: str
    tokens_reward: int = 15
    category: str


@dataclass
class UserProfile:
    """Represents user profile and progress"""
    username: str
    total_tokens: int
    quizzes_completed: int
    videos_watched: int
    streak_days: int
    completed_video_ids: List[int]
    completed_quiz_ids: List[int]


# ============================================================================
# SAMPLE DATA
# ============================================================================

SAMPLE_VIDEOS = [
    VideoShort(
        id=1,
        title_ar="أساسيات الحسابات السريعة",
        title_en="Quick Calculation Basics",
        duration=45,
        thumbnail="🎥",
        category="Quantitative",
        tokens_reward=15
    ),
    VideoShort(
        id=2,
        title_ar="مهارات الفهم القرائي",
        title_en="Reading Comprehension Skills",
        duration=60,
        thumbnail="📖",
        category="Qualitative",
        tokens_reward=15
    ),
    VideoShort(
        id=3,
        title_ar="تقنيات حل المسائل",
        title_en="Problem-Solving Techniques",
        duration=50,
        thumbnail="🧮",
        category="Quantitative",
        tokens_reward=15
    ),
    VideoShort(
        id=4,
        title_ar="المنطق والاستدلال",
        title_en="Logic and Reasoning",
        duration=55,
        thumbnail="🧠",
        category="Qualitative",
        tokens_reward=15
    ),
]

SAMPLE_QUIZZES = [
    QuizQuestion(
        id=1,
        question_ar="إذا كان 2 + 2 = ؟",
        question_en="If 2 + 2 = ?",
        options=["2", "3", "4", "5"],
        correct_answer_index=2,
        category="Quantitative",
        difficulty="Easy",
        tokens_reward=25
    ),
    QuizQuestion(
        id=2,
        question_ar="ما هو 15% من 200؟",
        question_en="What is 15% of 200?",
        options=["15", "30", "45", "60"],
        correct_answer_index=2,
        category="Quantitative",
        difficulty="Medium",
        tokens_reward=25
    ),
    QuizQuestion(
        id=3,
        question_ar="ما مرادف كلمة 'السعي'؟",
        question_en="What is a synonym for 'effort'?",
        options=["الكسل", "الاجتهاد", "الراحة", "الخمول"],
        correct_answer_index=1,
        category="Qualitative",
        difficulty="Medium",
        tokens_reward=25
    ),
    QuizQuestion(
        id=4,
        question_ar="إذا كانت النسبة 3:5 وقيمة الأول 12، فما قيمة الثاني؟",
        question_en="If ratio is 3:5 and first value is 12, what is the second value?",
        options=["15", "20", "25", "30"],
        correct_answer_index=1,
        category="Quantitative",
        difficulty="Hard",
        tokens_reward=25
    ),
]

OFFICIAL_RULES = [
    {
        "title_ar": "موعد الوصول",
        "title_en": "Arrival Time",
        "description_ar": "يجب الوصول قبل الموعد المحدد بـ 30 دقيقة على الأقل",
        "description_en": "Must arrive at least 30 minutes before the scheduled time",
        "icon": "⏰"
    },
    {
        "title_ar": "الهوية الوطنية",
        "title_en": "National ID",
        "description_ar": "إحضار الهوية الوطنية الأصلية إلزامي",
        "description_en": "Original National ID is mandatory",
        "icon": "🪪"
    },
    {
        "title_ar": "المواد المسموحة",
        "title_en": "Allowed Materials",
        "description_ar": "لا يسمح بإحضار أي أجهزة إلكترونية أو مراجع",
        "description_en": "No electronic devices or references allowed",
        "icon": "📵"
    },
    {
        "title_ar": "الملابس الرسمية",
        "title_en": "Formal Attire",
        "description_ar": "يفضل ارتداء ملابس رسمية ومحتشمة",
        "description_en": "Formal and modest clothing is preferred",
        "icon": "👔"
    },
    {
        "title_ar": "فترة الاختبار",
        "title_en": "Test Duration",
        "description_ar": "الاختبار يستمر لمدة ساعتين ونصف تقريباً",
        "description_en": "Test lasts approximately 2.5 hours",
        "icon": "⏱️"
    },
    {
        "title_ar": "البيانات الشخصية",
        "title_en": "Personal Data",
        "description_ar": "تأكد من صحة جميع بيانات المختبر",
        "description_en": "Ensure all personal data is correct",
        "icon": "✅"
    },
]

# ============================================================================
# MAIN APP CLASS
# ============================================================================

class NexoraApp:
    """Main Nexora Application Controller"""
    
    def __init__(self):
        self.user = UserProfile(
            username="مستخدم",
            total_tokens=250,
            quizzes_completed=0,
            videos_watched=0,
            streak_days=0,
            completed_video_ids=[],
            completed_quiz_ids=[]
        )
        self.current_page: Optional[str] = None
        self.is_rtl = True
        self.is_dark_mode = True
        
    def get_primary_color(self) -> str:
        """Royal Green"""
        return ft.colors.GREEN_700
    
    def get_accent_color(self) -> str:
        """Royal Amber/Gold"""
        return ft.colors.AMBER_400
    
    def get_background_color(self) -> str:
        """Dark background"""
        return "#1a1a1a"
    
    def add_tokens(self, amount: int) -> None:
        """Add tokens to user profile"""
        self.user.total_tokens += amount
    
    def get_tokens_display(self) -> str:
        """Get formatted token display"""
        return f"💎 {self.user.total_tokens}"


# ============================================================================
# UI COMPONENTS
# ============================================================================

class TokenBadge(ft.Container):
    """Token display badge component"""
    
    def __init__(self, tokens: int, app: NexoraApp):
        super().__init__()
        self.app = app
        self.tokens = tokens
        
        self.content = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        name=ft.icons.STAR,
                        color=app.get_accent_color(),
                        size=20
                    ),
                    ft.Text(
                        value=str(tokens),
                        size=16,
                        weight="bold",
                        color=app.get_accent_color()
                    ),
                ],
                spacing=5,
            ),
            padding=ft.padding.symmetric(10, 15),
            bgcolor=app.get_primary_color(),
            border_radius=20,
        )
    
    def update_tokens(self, new_tokens: int):
        """Update token display"""
        self.tokens = new_tokens
        self.content.content.controls[1].value = str(new_tokens)
        self.update()


class VideoCard(ft.Container):
    """Video short card component"""
    
    def __init__(self, video: VideoShort, app: NexoraApp, on_complete: Callable):
        super().__init__()
        self.video = video
        self.app = app
        self.on_complete = on_complete
        self.is_completed = video.id in app.user.completed_video_ids
        self.is_watched = False
        
        # Watch button
        self.watch_button = ft.ElevatedButton(
            text="مشاهدة" if app.is_rtl else "Watch",
            icon=ft.icons.PLAY_CIRCLE,
            on_click=self._on_watch_click,
            style=ft.ButtonStyle(
                bgcolor=app.get_primary_color(),
                color="white",
            ),
        )
        
        if self.is_completed:
            self.watch_button.disabled = True
            self.watch_button.text = "مكتمل ✓" if app.is_rtl else "Completed ✓"
            self.watch_button.icon = ft.icons.CHECK_CIRCLE
        
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text(
                            value=self.video.thumbnail,
                            size=48,
                        ),
                        alignment=ft.alignment.center,
                        height=120,
                        bgcolor=app.get_accent_color(),
                        border_radius=12,
                    ),
                    ft.Text(
                        value=video.title_ar if app.is_rtl else video.title_en,
                        size=14,
                        weight="bold",
                        text_align=ft.TextAlign.RIGHT if app.is_rtl else ft.TextAlign.LEFT,
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.ACCESS_TIME, size=14),
                            ft.Text(value=f"{video.duration}s", size=12),
                        ],
                        spacing=5,
                    ),
                    ft.Row(
                        controls=[
                            ft.Icon(
                                name=ft.icons.STAR,
                                color=app.get_accent_color(),
                                size=14
                            ),
                            ft.Text(
                                value=f"+{video.tokens_reward}",
                                size=12,
                                color=app.get_accent_color(),
                                weight="bold"
                            ),
                        ],
                        spacing=5,
                    ),
                    self.watch_button,
                ],
                spacing=8,
            ),
            padding=15,
            bgcolor="#2a2a2a",
            border_radius=12,
            border=ft.border.all(1, app.get_primary_color()),
        )
    
    def _on_watch_click(self, e):
        """Handle watch button click"""
        self.is_watched = True
        self.watch_button.disabled = True
        self.watch_button.text = "مكتمل ✓" if self.app.is_rtl else "Completed ✓"
        self.watch_button.icon = ft.icons.CHECK_CIRCLE
        
        # Mark as completed
        self.app.user.completed_video_ids.append(self.video.id)
        self.app.user.videos_watched += 1
        self.app.add_tokens(self.video.tokens_reward)
        
        self.update()
        self.on_complete()


class QuizCard(ft.Container):
    """Interactive quiz question card"""
    
    def __init__(self, quiz: QuizQuestion, app: NexoraApp, on_complete: Callable):
        super().__init__()
        self.quiz = quiz
        self.app = app
        self.on_complete = on_complete
        self.is_completed = quiz.id in app.user.completed_quiz_ids
        self.selected_index: Optional[int] = None
        self.feedback_text = ft.Text(value="", size=12, weight="bold")
        self.option_buttons: List[ft.OutlinedButton] = []
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the quiz UI"""
        # Question text
        question = ft.Container(
            content=ft.Text(
                value=self.quiz.question_ar if self.app.is_rtl else self.quiz.question_en,
                size=16,
                weight="bold",
                text_align=ft.TextAlign.RIGHT if self.app.is_rtl else ft.TextAlign.LEFT,
            ),
            padding=15,
            bgcolor="#2a2a2a",
            border_radius=12,
        )
        
        # Options
        options_column = ft.Column(spacing=10)
        for idx, option in enumerate(self.quiz.options):
            btn = ft.OutlinedButton(
                text=option,
                width=300,
                on_click=lambda e, i=idx: self._handle_answer(i),
                style=ft.ButtonStyle(
                    color=ft.colors.WHITE,
                ),
            )
            if self.is_completed:
                btn.disabled = True
            self.option_buttons.append(btn)
            options_column.controls.append(btn)
        
        # Difficulty badge
        difficulty_colors = {
            "Easy": ft.colors.GREEN_400,
            "Medium": ft.colors.AMBER_400,
            "Hard": ft.colors.RED_400,
        }
        
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Chip(
                                label=ft.Text(
                                    self.quiz.difficulty,
                                    size=11,
                                ),
                                bgcolor=difficulty_colors.get(self.quiz.difficulty, ft.colors.GREY),
                            ),
                            ft.Chip(
                                label=ft.Text(
                                    f"+{self.quiz.tokens_reward}",
                                    color=self.app.get_accent_color(),
                                    size=11,
                                ),
                                icon=ft.icons.STAR,
                            ),
                        ],
                        spacing=10,
                    ),
                    question,
                    options_column,
                    self.feedback_text,
                ],
                spacing=10,
            ),
            padding=15,
            bgcolor="#1f1f1f",
            border_radius=12,
            border=ft.border.all(1, self.app.get_primary_color()),
        )
    
    def _handle_answer(self, selected_index: int):
        """Handle answer selection"""
        if self.selected_index is not None or self.is_completed:
            return  # Prevent multiple answers
        
        self.selected_index = selected_index
        is_correct = selected_index == self.quiz.correct_answer_index
        
        # Visual feedback for all buttons
        for idx, btn in enumerate(self.option_buttons):
            btn.disabled = True
            if idx == self.quiz.correct_answer_index:
                btn.style.bgcolor = ft.colors.GREEN_700
                btn.style.color = "white"
            elif idx == selected_index and not is_correct:
                btn.style.bgcolor = ft.colors.RED_700
                btn.style.color = "white"
        
        # Feedback message
        if is_correct:
            self.feedback_text.value = "✓ إجابة صحيحة! +25 نقطة" if self.app.is_rtl else "✓ Correct! +25 points"
            self.feedback_text.color = ft.colors.GREEN_400
            self.app.add_tokens(self.quiz.tokens_reward)
        else:
            self.feedback_text.value = "✗ إجابة خاطئة" if self.app.is_rtl else "✗ Incorrect"
            self.feedback_text.color = ft.colors.RED_400
        
        # Mark as completed
        self.app.user.completed_quiz_ids.append(self.quiz.id)
        self.app.user.quizzes_completed += 1
        self.is_completed = True
        
        self.update()
        self.on_complete()


class RuleCard(ft.Container):
    """Official rule information card"""
    
    def __init__(self, rule: dict, app: NexoraApp):
        super().__init__()
        self.app = app
        self.rule = rule
        
        self.content = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                value=rule["icon"],
                                size=32,
                            ),
                            ft.Text(
                                value=rule["title_ar"] if app.is_rtl else rule["title_en"],
                                size=14,
                                weight="bold",
                            ),
                        ],
                        spacing=12,
                    ),
                    ft.Text(
                        value=rule["description_ar"] if app.is_rtl else rule["description_en"],
                        size=12,
                        text_align=ft.TextAlign.RIGHT if app.is_rtl else ft.TextAlign.LEFT,
                    ),
                ],
                spacing=8,
            ),
            padding=15,
            bgcolor="#2a2a2a",
            border_radius=12,
            border=ft.border.left(4, app.get_primary_color()) if app.is_rtl else ft.border.right(4, app.get_primary_color()),
        )


# ============================================================================
# PAGES
# ============================================================================

class HomePage(ft.Container):
    """Home/Dashboard page"""
    
    def __init__(self, app: NexoraApp, on_navigate: Callable):
        super().__init__()
        self.app = app
        self.on_navigate = on_navigate
        
        # Token badge
        self.token_badge = TokenBadge(app.user.total_tokens, app)
        
        self._build_ui()
    
    def _build_ui(self):
        """Build home page UI"""
        self.content = ft.ListView(
            controls=[
                # Header
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        value="نكسورا" if self.app.is_rtl else "NEXORA",
                                        size=32,
                                        weight="bold",
                                        color=self.app.get_primary_color(),
                                    ),
                                    ft.Icon(
                                        name=ft.icons.ROCKET,
                                        color=self.app.get_accent_color(),
                                        size=32,
                                    ),
                                ],
                                spacing=10,
                            ),
                            ft.Text(
                                value="مرحباً بك في منصة تحضيرك للقيّاس والتحصيلي" if self.app.is_rtl else "Welcome to Your Qiyas & Tahseeli Prep Platform",
                                size=14,
                                color=ft.colors.GREY_400,
                            ),
                        ],
                        spacing=8,
                    ),
                    padding=20,
                ),
                
                # User Stats
                ft.Container(
                    content=ft.Row(
                        controls=[
                            self.token_badge,
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value=str(self.app.user.videos_watched), size=18, weight="bold"),
                                        ft.Text(value="فيديوهات" if self.app.is_rtl else "Videos", size=11, color=ft.colors.GREY_400),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                padding=15,
                                bgcolor="#2a2a2a",
                                border_radius=12,
                                border=ft.border.all(1, self.app.get_primary_color()),
                            ),
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value=str(self.app.user.quizzes_completed), size=18, weight="bold"),
                                        ft.Text(value="اختبارات" if self.app.is_rtl else "Quizzes", size=11, color=ft.colors.GREY_400),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                padding=15,
                                bgcolor="#2a2a2a",
                                border_radius=12,
                                border=ft.border.all(1, self.app.get_primary_color()),
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=20,
                ),
                
                # Quick Action Buttons
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.ElevatedButton(
                                text="فيديوهات تعليمية" if self.app.is_rtl else "Smart Shorts",
                                icon=ft.icons.PLAY_CIRCLE,
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    bgcolor=self.app.get_primary_color(),
                                    color="white",
                                ),
                                on_click=lambda e: self.on_navigate("videos"),
                            ),
                            ft.ElevatedButton(
                                text="اختبارات تدريبية" if self.app.is_rtl else "Practice Quiz",
                                icon=ft.icons.QUIZ,
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    bgcolor=self.app.get_accent_color(),
                                    color=ft.colors.BLACK,
                                ),
                                on_click=lambda e: self.on_navigate("quiz"),
                            ),
                            ft.ElevatedButton(
                                text="القوانين الرسمية" if self.app.is_rtl else "Official Rules",
                                icon=ft.icons.INFO,
                                width=300,
                                height=50,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.colors.BLUE_700,
                                    color="white",
                                ),
                                on_click=lambda e: self.on_navigate("rules"),
                            ),
                        ],
                        spacing=12,
                    ),
                    padding=20,
                ),
                
                # Motivational Section
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="💪 نصيحة اليوم" if self.app.is_rtl else "💪 Tip of the Day",
                                size=14,
                                weight="bold",
                            ),
                            ft.Text(
                                value="مارس الاختبارات بانتظام واكسب المكافآت!" if self.app.is_rtl else "Practice regularly and earn rewards!",
                                size=12,
                                color=ft.colors.GREY_400,
                            ),
                        ],
                        spacing=8,
                    ),
                    padding=15,
                    bgcolor="#2a2a2a",
                    border_radius=12,
                    border=ft.border.all(1, self.app.get_accent_color()),
                ),
                
                ft.SizedBox(height=30),
            ],
            expand=True,
            spacing=10,
            padding=0,
        )
    
    def update_tokens(self, new_tokens: int):
        """Update displayed tokens"""
        self.token_badge.update_tokens(new_tokens)


class VideosPage(ft.Container):
    """Videos/Smart Shorts page"""
    
    def __init__(self, app: NexoraApp, on_navigate: Callable):
        super().__init__()
        self.app = app
        self.on_navigate = on_navigate
        self.home_ref: Optional[HomePage] = None
        
        self._build_ui()
    
    def _build_ui(self):
        """Build videos page UI"""
        videos_column = ft.Column(spacing=12)
        
        for video in SAMPLE_VIDEOS:
            card = VideoCard(
                video,
                self.app,
                on_complete=self._on_video_complete
            )
            videos_column.controls.append(card)
        
        self.content = ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda e: self.on_navigate("home"),
                            ),
                            ft.Text(
                                value="فيديوهات تعليمية" if self.app.is_rtl else "Educational Shorts",
                                size=20,
                                weight="bold",
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=15,
                ),
                ft.Container(
                    content=videos_column,
                    padding=15,
                ),
                ft.SizedBox(height=30),
            ],
            expand=True,
            spacing=0,
            padding=0,
        )
    
    def _on_video_complete(self):
        """Handle video completion"""
        if self.home_ref:
            self.home_ref.update_tokens(self.app.user.total_tokens)


class QuizPage(ft.Container):
    """Quiz page"""
    
    def __init__(self, app: NexoraApp, on_navigate: Callable):
        super().__init__()
        self.app = app
        self.on_navigate = on_navigate
        self.home_ref: Optional[HomePage] = None
        
        self._build_ui()
    
    def _build_ui(self):
        """Build quiz page UI"""
        quiz_column = ft.Column(spacing=15)
        
        for quiz in SAMPLE_QUIZZES:
            card = QuizCard(
                quiz,
                self.app,
                on_complete=self._on_quiz_complete
            )
            quiz_column.controls.append(card)
        
        self.content = ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda e: self.on_navigate("home"),
                            ),
                            ft.Text(
                                value="اختبارات تدريبية" if self.app.is_rtl else "Practice Quiz",
                                size=20,
                                weight="bold",
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=15,
                ),
                ft.Container(
                    content=quiz_column,
                    padding=15,
                ),
                ft.SizedBox(height=30),
            ],
            expand=True,
            spacing=0,
            padding=0,
        )
    
    def _on_quiz_complete(self):
        """Handle quiz completion"""
        if self.home_ref:
            self.home_ref.update_tokens(self.app.user.total_tokens)


class RulesPage(ft.Container):
    """Official Rules page"""
    
    def __init__(self, app: NexoraApp, on_navigate: Callable):
        super().__init__()
        self.app = app
        self.on_navigate = on_navigate
        
        self._build_ui()
    
    def _build_ui(self):
        """Build rules page UI"""
        rules_column = ft.Column(spacing=12)
        
        for rule in OFFICIAL_RULES:
            card = RuleCard(rule, self.app)
            rules_column.controls.append(card)
        
        self.content = ft.ListView(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                on_click=lambda e: self.on_navigate("home"),
                            ),
                            ft.Text(
                                value="القوانين الرسمية" if self.app.is_rtl else "Official Rules",
                                size=20,
                                weight="bold",
                            ),
                        ],
                        spacing=10,
                    ),
                    padding=15,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                value="تعليمات مهمة ليوم الاختبار" if self.app.is_rtl else "Important Instructions for Test Day",
                                size=14,
                                weight="bold",
                                color=self.app.get_accent_color(),
                            ),
                        ],
                        spacing=8,
                    ),
                    padding=15,
                ),
                ft.Container(
                    content=rules_column,
                    padding=15,
                ),
                ft.SizedBox(height=30),
            ],
            expand=True,
            spacing=0,
            padding=0,
        )


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main(page: ft.Page):
    """Main application entry point"""
    
    # Page configuration
    page.title = "Nexora - Qiyas Prep"
    page.theme_mode = ft.ThemeMode.DARK
    page.rtl = True
    page.window_width = 400
    page.window_height = 800
    page.padding = 0
    
    # Initialize app
    app = NexoraApp()
    
    # Create pages
    home_page = HomePage(app, on_navigate=lambda page_name: navigate_to(page_name))
    videos_page = VideosPage(app, on_navigate=lambda page_name: navigate_to(page_name))
    quiz_page = QuizPage(app, on_navigate=lambda page_name: navigate_to(page_name))
    rules_page = RulesPage(app, on_navigate=lambda page_name: navigate_to(page_name))
    
    # Set cross-references for token updates
    videos_page.home_ref = home_page
    quiz_page.home_ref = home_page
    
    pages = {
        "home": home_page,
        "videos": videos_page,
        "quiz": quiz_page,
        "rules": rules_page,
    }
    
    def navigate_to(page_name: str):
        """Navigate to a specific page"""
        app.current_page = page_name
        page.clean()
        page.add(pages[page_name])
    
    # Set custom theme
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=app.get_primary_color(),
            secondary=app.get_accent_color(),
            background=app.get_background_color(),
        )
    )
    
    # Start on home page
    navigate_to("home")


if __name__ == "__main__":
    ft.app(target=main)
