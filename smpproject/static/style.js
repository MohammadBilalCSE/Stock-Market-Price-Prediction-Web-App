// Function to toggle theme
function toggleTheme() {
  var iconElement = document.querySelector(
    ".settings_right .changeTheme button i"
  );
  var isDarkMode = document.body.classList.contains("dark-mode");

  if (isDarkMode) {
    // Switch to light mode
    document.body.classList.remove("dark-mode");
    localStorage.setItem("theme", "light");
    if (iconElement) {
      iconElement.classList.remove("bi-sun-fill");
      iconElement.classList.add("bi-moon-fill");
    }
  } else {
    // Switch to dark mode
    document.body.classList.add("dark-mode");
    localStorage.setItem("theme", "dark");
    if (iconElement) {
      iconElement.classList.remove("bi-moon-fill");
      iconElement.classList.add("bi-sun-fill");
    }
  }

  // Apply the theme to other templates
  applyThemeToOtherTemplates();
}

function applyThemeToOtherTemplates() {
  var theme = localStorage.getItem("theme");
  var otherTemplates = document.querySelectorAll(".theme-aware-element");

  otherTemplates.forEach(function (template) {
    if (theme === "dark") {
      template.classList.add("dark-mode");
    } else {
      template.classList.remove("dark-mode");
    }
  });
}

// Function to apply the stored theme preference
function applyStoredTheme() {
  var theme = localStorage.getItem("theme");
  if (theme === "dark") {
    document.body.classList.add("dark-mode");
    var iconElement = document.querySelector(
      ".settings_right .changeTheme button i"
    );
    if (iconElement) {
      iconElement.classList.remove("bi-moon-fill");
      iconElement.classList.add("bi-sun-fill");
    }
  }
}

// Toggle theme when clicking on the theme button
function myFunction() {
  toggleTheme();
}

// Apply stored theme preference when the DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  applyStoredTheme();
});
