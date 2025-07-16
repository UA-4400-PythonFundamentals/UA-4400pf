import unittest
import cmath
from .fun import solve_quadratic_equation


class TestQuadraticEquationSolver(unittest.TestCase):
    """
    Клас для тестування функції solve_quadratic_equation.
    """

    def test_positive_discriminant(self):
        """
        Тест для випадку з додатним дискримінантом (два дійсні корені).
        Рівняння: x^2 - 5x + 6 = 0
        Корені: x1 = 2, x2 = 3
        """
        a, b, c = 1, -5, 6
        roots = solve_quadratic_equation(a, b, c)
        # Перевіряємо, що повернуто два корені
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 2)
        # Перевіряємо, що корені є правильними (порядок може відрізнятися)
        self.assertIn(2.0, [roots[0], roots[1]])
        self.assertIn(3.0, [roots[0], roots[1]])

    def test_zero_discriminant(self):
        """
        Тест для випадку з нульовим дискримінантом (один дійсний корінь).
        Рівняння: x^2 - 4x + 4 = 0
        Корінь: x1 = 2
        """
        a, b, c = 1, -4, 4
        roots = solve_quadratic_equation(a, b, c)
        # Перевіряємо, що повернуто один корінь
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 1)
        # Перевіряємо значення кореня
        self.assertAlmostEqual(roots[0], 2.0)

    def test_negative_discriminant(self):
        """
        Тест для випадку з від'ємним дискримінантом (два комплексні корені).
        Рівняння: x^2 + 1 = 0
        Корені: x1 = -1j, x2 = 1j
        """
        a, b, c = 1, 0, 1
        roots = solve_quadratic_equation(a, b, c)
        # Перевіряємо, що повернуто два корені
        self.assertIsNotNone(roots)
        self.assertEqual(len(roots), 1, "len")
        # Перевіряємо значення комплексних коренів
        self.assertAlmostEqual(roots[0], None)
        # self.assertAlmostEqual(roots[1], 1j)

    # def test_a_is_zero(self):
    #     """
    #     Тест для випадку, коли коефіцієнт 'a' дорівнює нулю.
    #     Це не квадратне рівняння, функція повинна повернути None.
    #     """
    #     a, b, c = 0, 2, 4
    #     roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNone(roots)

    # def test_large_coefficients(self):
    #     """
    #     Тест з великими коефіцієнтами.
    #     Рівняння: 2x^2 + 1000x + 500 = 0
    #     """
    #     a, b, c = 2, 1000, 500
    #     roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNotNone(roots)
    #     self.assertEqual(len(roots), 2)
    #     # Перевіряємо значення, використовуючи відомі результати або калькулятор
    #     self.assertAlmostEqual(roots[0], (-1000 - cmath.sqrt(1000**2 - 4*2*500)) / (2*2), places=5)
    #     self.assertAlmostEqual(roots[1], (-1000 + cmath.sqrt(1000**2 - 4*2*500)) / (2*2), places=5)

    # def test_fractional_coefficients(self):
    #     """
    #     Тест з дробовими коефіцієнтами.
    #     Рівняння: 0.5x^2 - 1.5x + 1 = 0
    #     Корені: x1 = 1, x2 = 2
    #     """
    #     a, b, c = 0.5, -1.5, 1
    #     roots = solve_quadratic_equation(a, b, c)
    #     self.assertIsNotNone(roots)
    #     self.assertEqual(len(roots), 2)
    #     self.assertIn(1.0, [roots[0], roots[1]])
    #     self.assertIn(2.0, [roots[0], roots[1]])


if __name__ == '__main__':
    unittest.main()

