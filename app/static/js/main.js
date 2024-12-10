let currentLanguage = "en";

function toggleLanguage() {
    const toggle = document.querySelector(".toggle-switch");
    const circle = document.querySelector(".toggle-switch-circle");

    if (toggle.classList.contains("hindi")) {
        toggle.classList.remove("hindi");
        toggle.classList.add("urdu");
        currentLanguage = "ur";
    } else if (toggle.classList.contains("urdu")) {
        toggle.classList.remove("urdu");
        currentLanguage = "en";
    } else {
        toggle.classList.add("hindi");
        currentLanguage = "hi";
    }
    updateLanguage();
}

function updateLanguage() {
    const elements = {
        heading: document.querySelector("h1"),
        likeBtn: document.querySelector("#like-btn"),
        dislikeBtn: document.querySelector("#dislike-btn"),
        footer: document.querySelector("footer"),
        formHeading: document.querySelector("#form-heading"),
        nameField: document.querySelector("#name-field"),
        mobileField: document.querySelector("#mobile-field"),
        feedbackField: document.querySelector("#feedback-field"),
        submitButton: document.querySelector("#submit-button")
    };

    const translations = {
        hi: {
            heading: "आपका अनुभव कैसा रहा?",
            like: "👍 पसंद",
            dislike: "👎 नापसंद",
            footer: "प्यार के साथ बनाया गया ❤️ फरिज़ अंजुम द्वारा",
            formHeading: "कृपया अपनी प्रतिक्रिया दर्ज करें:",
            name: "आपका नाम (वैकल्पिक)",
            mobile: "अपना मोबाइल नंबर दर्ज करें",
            feedback: "अपनी प्रतिक्रिया दर्ज करें",
            submit: "प्रस्तुत करें"
        },
        ur: {
            heading: "آپ کا تجربہ کیسا رہا؟",
            like: "👍 پسند",
            dislike: "👎 ناپسند",
            footer: "محبت کے ساتھ بنایا گیا ❤️ فاریز انجم کے ذریعہ",
            formHeading: "براہ کرم اپنی رائے درج کریں:",
            name: "آپ کا نام (اختیاری)",
            mobile: "اپنا موبائل نمبر درج کریں",
            feedback: "اپنی رائے درج کریں",
            submit: "جمع کرائیں"
        },
        en: {
            heading: "How was your experience?",
            like: "👍 Like",
            dislike: "👎 Dislike",
            footer: "Made with ❤️ by Fariz Anjum",
            formHeading: "Please provide your feedback:",
            name: "Your name (optional)",
            mobile: "Enter your mobile number",
            feedback: "Enter your feedback",
            submit: "Submit"
        }
    };

    const current = translations[currentLanguage];
    
    if (elements.heading) elements.heading.innerText = current.heading;
    if (elements.likeBtn) elements.likeBtn.innerText = current.like;
    if (elements.dislikeBtn) elements.dislikeBtn.innerText = current.dislike;
    if (elements.footer) elements.footer.innerHTML = current.footer;
    if (elements.formHeading) elements.formHeading.innerText = current.formHeading;
    if (elements.nameField) elements.nameField.placeholder = current.name;
    if (elements.mobileField) elements.mobileField.placeholder = current.mobile;
    if (elements.feedbackField) elements.feedbackField.placeholder = current.feedback;
    if (elements.submitButton) elements.submitButton.innerText = current.submit;
}

function handleLike() {
    document.body.innerHTML = `
        <h1>Show us some love on Google Reviews!</h1>
        <div class="stars">
            <span>⭐</span>
            <span>⭐</span>
            <span>⭐</span>
            <span>⭐</span>
            <span>⭐</span>
        </div>
        <p>Help us stay the best! Your 5-star review means the world to us! 🌟</p>
        <p>Redirecting to Google Reviews...</p>
    `;
    setTimeout(() => {
        const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);
        const reviewUrl = "https://g.page/r/CQWF4a4gLoi2EBM/review";
        window.location.href = reviewUrl;
    }, 3000);
}

function handleDislike() {
    if (confirm("Are you sure you want to dislike?")) {
        window.location.href = "/feedback";
    }
} 