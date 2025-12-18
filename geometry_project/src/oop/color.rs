#[derive(Debug, Clone)]
pub struct Color {
    name_ru: String,
}

impl Color {
    pub fn new(name_ru: &str) -> Self {
        Self {
            name_ru: name_ru.to_string(),
        }
    }

    pub fn get_name_ru(&self) -> &str {
        &self.name_ru
    }

    pub fn blue() -> Self {
        Self::new("синий")
    }

    pub fn green() -> Self {
        Self::new("зеленый")
    }

    pub fn red() -> Self {
        Self::new("красный")
    }
}
