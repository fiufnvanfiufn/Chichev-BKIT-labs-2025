use super::{GeometricShape, Color};

pub struct Rectangle {
    width: f64,
    height: f64,
    color: Color,
}

impl Rectangle {
    pub fn new(width: f64, height: f64, color: Color) -> Self {
        Self { width, height, color }
    }
}

impl GeometricShape for Rectangle {
    fn area(&self) -> f64 {
        self.width * self.height
    }

    fn shape_name(&self) -> &'static str {
        "Прямоугольник"
    }
}
