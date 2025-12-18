mod oop;

use oop::{GeometricShape, Color, Rectangle, Circle, Square};

use colored::Colorize;

fn demonstrate_external_package() {
    println!("\n{}", "Демонстрация внешнего пакета colored:".bold());

    let n = 5;


    println!("{}", format!("Прямоугольник: ширина={}, высота={}", n, n).blue());
    println!("{}", format!("Круг: радиус={}", n).green());
    println!("{}", format!("Квадрат: сторона={}", n).red());

    println!("{}", "Цветной текст с использованием внешнего пакета!".cyan().bold());
}

fn main() {
    println!("{}", "=== Геометрический проект на Rust ===".bold().underline());

    let n = 5.0;



    let rectangle = Rectangle::new(n, n, Color::blue());
    let circle = Circle::new(n, Color::green());
    let square = Square::new(n, Color::red());


    println!("\n{}", "Геометрические фигуры:".bold());
    println!("1. {}", rectangle.repr());
    println!("2. {}", circle.repr());
    println!("3. {}", square.repr());


    demonstrate_external_package();

    println!("\n{}", "Программа успешно выполнена!".green());
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_rectangle() {
        let rect = Rectangle::new(3.0, 4.0, Color::blue());
        assert_eq!(rect.area(), 12.0);
    }
}
