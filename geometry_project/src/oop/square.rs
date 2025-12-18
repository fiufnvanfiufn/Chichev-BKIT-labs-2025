use super::{GeometricShape, Color, Rectangle};

pub struct Square {
    rectangle: Rectangle,
}

impl Square {
    pub fn new(side: f64, color: Color) -> Self {
        Self {
            rectangle: Rectangle::new(side, side, color),
        }
    }
}

impl GeometricShape for Square {
    fn area(&self) -> f64 {
        self.rectangle.area()
    }

    fn shape_name(&self) -> &'static str {
        "Квадрат"
    }
}
