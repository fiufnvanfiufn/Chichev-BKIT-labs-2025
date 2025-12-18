use super::color::Color;

pub trait GeometricShape {
    fn area(&self) -> f64;
    fn shape_name(&self) -> &'static str;

    fn repr(&self) -> String {
        format!("{}: площадь = {:.2}", self.shape_name(), self.area())
    }
}
