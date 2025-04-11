// Получаем canvas
const canvas = document.getElementById('snow');
const ctx = canvas.getContext('2d');

// Устанавливаем размеры canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

// Массив снежинок
const snowflakes = [];

// Функция для создания снежинок
function createSnowflakes() {
    const x = Math.random() * canvas.width;
    const y = Math.random() * canvas.height;
    const radius = Math.random() * 3 + 1; // Размер снежинки
    const speed = Math.random() * 1 + 0.5; // Скорость падения

    snowflakes.push({ x, y, radius, speed });
}

// Анимация снежинок
function drawSnowflakes() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    snowflakes.forEach((flake, index) => {
        ctx.beginPath();
        ctx.arc(flake.x, flake.y, flake.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'white';
        ctx.fill();

        // Обновляем позицию
        flake.y += flake.speed;

        // Если снежинка уходит за пределы экрана
        if (flake.y > canvas.height) {
            snowflakes.splice(index, 1);
        }
    });

    // Добавляем больше снежинок
    if (snowflakes.length < 100) {
        createSnowflakes();
    }

    requestAnimationFrame(drawSnowflakes);
}

// Обработка изменения размера экрана
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});

// Запуск анимации
drawSnowflakes();
ScrollReveal().reveal('.reveal', {
  distance: '50px',
  duration: 1000,
  easing: 'ease-in-out',
  origin: 'bottom',
  interval: 200,
});
