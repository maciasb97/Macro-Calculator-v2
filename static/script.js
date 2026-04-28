/* ══════════════════════════════════════════════ MAIN SCRIPT FILE ══════════════════════════════════════════════ */
import { resultTabs } from "./tabs.js";

document.addEventListener('DOMContentLoaded', function() {
    // Only run resultTabs() if we're on the results page
    if (document.querySelector('.results-card')) {
        resultTabs();
    }
});