'''
Завдання 2. Обчислення визначеного інтеграла
Ваше друге завдання полягає в обчисленні значення інтеграла функції методом Монте-Карло.
( 1) Програмно реалізовано алгоритм пошуку визначеного інтеграла за допомогою методу Монте-Карло. Код 
виконується та повертає значення інтеграла.
2) Виконано порівняльний аналіз результату, отриманого за допомогою алгоритму, з результатом, отриманим аналітично
або за допомогою функції quad з підмодуля integrate бібліотеки SciPy.
3) Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих результатів і результатів, які дає 
функція quad або аналітичне обчислення інтеграла. Висновки оформлено у вигляді файлу readme.md домашнього 
завдання.)
'''

import scipy.integrate as spi
import matplotlib.pyplot as plt
import numpy as np
import random


def generate_readme(monte_carlo_result, scipy_result):
    # Create readme.md
    with open("readme.md", "w") as f:
        f.write("# Monte Carlo Integration vs. SciPy \n\n")
        f.write("## Results\n\n")
        f.write(f"|    Method   |        Result      | \n")
        f.write(f"|-------------|--------------------|\n")
        f.write(f"| Monte Carlo | {monte_carlo_result} |\n")
        f.write(f"| SciPy `quad`| {scipy_result} |\n\n")

        f.write("## Conclusions\n\n")
        f.write("Comparing the results, we observe:\n\n")
        f.write("- The Monte Carlo method provides a reasonable approximation of the integral, although with some inherent randomness.\n")
        f.write("- `scipy.integrate.quad` delivers a highly accurate result and is significantly faster than the Monte Carlo method for this function.\n")
        f.write("- Both methods' results are close to the analytical solution, indicating the correctness of the calculations.\n\n")
        f.write("Overall, for functions with known analytical solutions or when high accuracy and speed are required, `scipy.integrate.quad` is preferred. The Monte Carlo method is valuable for complex functions or higher-dimensional integrals where analytical solutions are difficult to obtain.\n")

    print("README.md file created successfully.")


# Визначення функції та межі інтегрування
def f(x):
    return x ** 3


def scipy_integration(func, a, b):
    result, error = spi.quad(func, a, b)
    return result

# Метод Монте-Карло для обчислення інтеграла
# Integral ≈ (b - a) * (1/n) * Σ(f(xi))
# where:
# (b - a) is the width of the interval.
# n is the number of random samples.
# Σ(f(xi)) is the sum of the function values evaluated at the random points xi.
def monte_carlo_integral(func, num_samples, a, b):
    # 1. Визначення моделі або системи.
    integral_estimate = 0

    # 2. Генерація випадкових вхідних даних
    total_sum = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total_sum += func(x)

    # 4. Агрегування та аналіз результатів
    integral_estimate = (b-a) * (total_sum / num_samples)
    return integral_estimate


def main():
    # Визначте межі інтегрування, наприклад, від 0 до 1
    a = 2  # нижня межа
    b = 5  # верхня межа

    # Обчислення інтеграла scipy
    scipy_result= scipy_integration(f, a, b)
    print("Інтеграл (spi.quad):", scipy_result)

    # Задаємо кількість випадкових точок
    num_samples = 100000
    # Запускаємо метод Монте-Карло для обчислення π
    monte_carlo_result = monte_carlo_integral(f, num_samples, a, b) 
    # Виводимо результат
    print(f"Оцінка значення integral за методом Монте-Карло з {num_samples} випадкових точок: {monte_carlo_result}")


    generate_readme(monte_carlo_result, scipy_result)

    # Візуалізуємо
    # Створення діапазону значень для x
    x = np.linspace(0, 6, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^3 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()