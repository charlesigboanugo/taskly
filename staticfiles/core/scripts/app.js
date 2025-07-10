import { initMobilemenu } from "./mobile-menu.js";
import { initThemeToggle} from "./theme-toggle.js";
import { initMessages } from "./messages.js";


window.onload = () => {
    console.log("nice")
    initMessages();
    initMobilemenu();
    initThemeToggle();
}