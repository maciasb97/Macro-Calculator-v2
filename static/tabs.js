/* ══════════════════════════════════════════════ TAB SWITCHING LOGIC ══════════════════════════════════════════════ */

export function resultTabs() {
    //querySelectorAll grabs every element with class="tab-btn" and class="tab-panel" and returns them as lists
    const buttons = document.querySelectorAll('.tab-btn');
    const panels  = document.querySelectorAll('.tab-panel');

    buttons.forEach(function(btn) {
        btn.addEventListener('click', function() {

            // Remove .active from ALL buttons and panels first
            buttons.forEach(function(b) { b.classList.remove('active'); });
            panels.forEach(function(p)  { p.classList.remove('active'); });

            // Add .active to the clicked button
            btn.classList.add('active');

            // btn.dataset.target reads the data-target="maintenance" attribute
            // document.getElementById finds the matching panel by that id
            document.getElementById(btn.dataset.target).classList.add('active');
        });
    });
}