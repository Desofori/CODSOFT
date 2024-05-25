document.addEventListener("DOMContentLoaded", () => {
    // Global Variables
    let questionCount = 0;
    let currentQuestionIndex = 0;
    let userAnswers = [];
    let quizKey = null;
    let quiz = null;

    // Home Page
    const homePage = document.querySelector('#homePage');
    if (homePage) {
        // Display welcome message and navigation options
    }

    // Quiz Creation Page
    const quizForm = document.getElementById('quizForm');
    if (quizForm) {
        document.getElementById('addQuestion').addEventListener('click', () => {
            questionCount++;
            const questionDiv = document.createElement('div');
            questionDiv.innerHTML = `
                <label for="question${questionCount}">Question ${questionCount}</label>
                <input type="text" id="question${questionCount}" name="question${questionCount}" required>
                <label>Options</label>
                <input type="text" name="option${questionCount}_1" placeholder="Option 1" required>
                <input type="text" name="option${questionCount}_2" placeholder="Option 2" required>
                <input type="text" name="option${questionCount}_3" placeholder="Option 3" required>
                <input type="text" name="option${questionCount}_4" placeholder="Option 4" required>
                <label for="correct${questionCount}">Correct Answer</label>
                <input type="text" id="correct${questionCount}" name="correct${questionCount}" required>
            `;
            document.getElementById('questionsContainer').appendChild(questionDiv);
        });

        quizForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const quizData = new FormData(e.target);
            const quiz = {
                questions: []
            };

            for (let i = 1; i <= questionCount; i++) {
                quiz.questions.push({
                    question: quizData.get(`question${i}`),
                    options: [
                        quizData.get(`option${i}_1`),
                        quizData.get(`option${i}_2`),
                        quizData.get(`option${i}_3`),
                        quizData.get(`option${i}_4`)
                    ],
                    correct: quizData.get(`correct${i}`)
                });
            }

            localStorage.setItem('quiz_' + Date.now(), JSON.stringify(quiz));
            alert('Quiz saved!');
            window.location.href = 'quiz_list.html';
        });
    }

    // Quiz List Page
    const quizList = document.getElementById('quizList');
    if (quizList) {
        for (let i = 0; i < localStorage.length; i++) {
            const key = localStorage.key(i);
            if (key.startsWith('quiz_')) {
                const quiz = JSON.parse(localStorage.getItem(key));
                const listItem = document.createElement('li');
                listItem.textContent = `Quiz ${i + 1}`;
                listItem.addEventListener('click', () => {
                    window.location.href = `quiz_take.html?quiz=${key}`;
                });
                quizList.appendChild(listItem);
            }
        }
    }

    // Quiz Taking Page
    const quizTitle = document.getElementById('quizTitle');
    const quizContainer = document.getElementById('quizContainer');
    const submitQuizButton = document.getElementById('submitQuiz');
    if (quizTitle && quizContainer && submitQuizButton) {
        const urlParams = new URLSearchParams(window.location.search);
        quizKey = urlParams.get('quiz');
        quiz = JSON.parse(localStorage.getItem(quizKey));

        quizTitle.textContent = 'Quiz';
        displayQuestion();

        function displayQuestion() {
            if (currentQuestionIndex >= quiz.questions.length) {
                submitQuizButton.style.display = 'block';
                return;
            }

            const question = quiz.questions[currentQuestionIndex];
            const questionDiv = document.createElement('div');
            questionDiv.innerHTML = `
                <h2>${question.question}</h2>
                ${question.options.map((option, index) => `
                    <label>
                        <input type="radio" name="question${currentQuestionIndex}" value="${option}" required>
                        ${option}
                    </label>
                `).join('')}
            `;
            quizContainer.innerHTML = '';
            quizContainer.appendChild(questionDiv);

            const radios = questionDiv.querySelectorAll('input[type="radio"]');
            radios.forEach(radio => {
                radio.addEventListener('change', () => {
                    userAnswers[currentQuestionIndex] = radio.value;
                    currentQuestionIndex++;
                    displayQuestion();
                });
            });
        }

        submitQuizButton.addEventListener('click', () => {
            let score = 0;
            quiz.questions.forEach((question, index) => {
                if (userAnswers[index] === question.correct) {
                    score++;
                }
            });
            alert(`Your score: ${score}/${quiz.questions.length}`);
            window.location.href = 'quiz_list.html';
        });
    }
});
