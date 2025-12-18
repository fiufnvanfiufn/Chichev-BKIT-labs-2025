use std::f64::consts::PI;
use super::{GeometricShape, Color};

pub struct Circle {
    radius: f64,
    color: Color,
}

impl Circle {
    pub fn new(radius: f64, color: Color) -> Self {
        Self { radius, color }
    }
}

impl GeometricShape for Circle {
    fn area(&self) -> f64 {
        PI * self.radius * self.radius
    }

    fn shape_name(&self) -> &'static str {
        "Круг"
    }
}
