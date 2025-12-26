mod oop;

use oop::{GeometricShape, Color, Rectangle, Circle, Square};

use colored::Colorize;

fn demonstrate_external_package() {
    println!("\n{}", "Демонстрация внешнего пакета colored:".bold());

    let n = 22.0;


    println!("{}", format!("Прямоугольник: ширина={}, высота={}", n, n).blue());
    println!("{}", format!("Круг: радиус={}", n).green());
    println!("{}", format!("Квадрат: сторона={}", n).red());

}

fn main() {

    let n = 22.0;

    let rectangle = Rectangle::new(n, n, Color::blue());
    let circle = Circle::new(n, Color::green());
    let square = Square::new(n, Color::red());


    println!("\n{}", "Геометрические фигуры:".bold());
    println!("1. {}", rectangle.repr());
    println!("2. {}", circle.repr());
    println!("3. {}", square.repr());


    demonstrate_external_package();
}
