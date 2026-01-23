document.addEventListener("DOMContentLoaded", () => {
    // Hide all full-content divs on page load
    const fullContents = document.querySelectorAll(".full-content");
    fullContents.forEach(div => div.style.display = "none");

    // Add toggle function to window so it works with onclick
    window.toggleReadMore = function(id) {
        const preview = document.getElementById(`preview-${id}`);
        const full = document.getElementById(`full-${id}`);
        const btn = document.getElementById(`btn-${id}`);

        if (full.style.display === "none" || full.style.display === "") {
            preview.style.display = "none";
            full.style.display = "block";
            btn.innerText = "Show Less ⬆️";
        } else {
            preview.style.display = "block";
            full.style.display = "none";
            btn.innerText = "Show More ⬇️";
        }
    }
});
