<script>
    import { currentMonth, currentTime} from "../utils"
    import Icons from "./Icons.svelte";
    import toast, { Toaster } from 'svelte-french-toast';

    import CalendarFill from "svelte-bootstrap-icons/lib/CalendarFill.svelte";
    import CalendarEventFill from "svelte-bootstrap-icons/lib/CalendarEventFill.svelte";
    import CircleHalf from "svelte-bootstrap-icons/lib/CircleHalf.svelte";
    import ClockFill from "svelte-bootstrap-icons/lib/ClockFill.svelte";
    import EyeSlashFill from "svelte-bootstrap-icons/lib/EyeSlashFill.svelte";

    export let filters;
    export let selectedGame;

    const monthNames = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    };

    const islandExclusive = "icons/tortimer-island-exclusive.png";
    const islandAvailable = "icons/tortimer-island-available.png"

    function filterButtonClick(bool) {
        // Make sure clicking current resets time and month to now
        // Also remove ignoreTime selection if true
        if (!filters.all && !bool) {
            filters.time = currentTime();
            filters.month = currentMonth();
            filters.ignoreTime = false;
        // When selecting all, reset caught and tortimer island
        // filter
        } else if (!filters.all && bool) {
            filters.hideCaught = false;
            filters.includeIsland = true;
        }
        filters.all = bool;
    }

    function navButtonClick(crittertype) {
        filters.crittertype = crittertype;
    }

    function ignoreTimeToggle() {
        filters.ignoreTime = !filters.ignoreTime;
    }

    function includeIslandToggle() {
        filters.includeIsland = !filters.includeIsland;
    }

    function hideCaughtToggle() {
        filters.hideCaught = !filters.hideCaught;
    }

    function markAsCaughtToggle() {
        if (!filters.markAsCaught) {
            toast("Click on critters to (un)set them as caught", {icon: "💭"})
        }
        filters.markAsCaught = !filters.markAsCaught;
    }

    function hemisphereToggle(value) {
        filters.northernHemisphere = value;
    }

</script>

<div class="filter-tabs">
    <div class="left" style="z-index: 1">
        <button class={ filters.crittertype == "bug" ? "nav-button active" : "nav-button"} on:click={() => {navButtonClick("bug")}}>
            <Icons name="bug" class="filter-icon"/>
        </button>
        <button class={ filters.crittertype == "fish" ? "nav-button active" : "nav-button"} on:click={() => {navButtonClick("fish")}}>
            <Icons name="fish" class="filter-icon"/>
        </button>
        {#if ["newhorizons", "newleaf"].includes(selectedGame)}
            <button class={ filters.crittertype == "sea_creature" ? "nav-button active" : "nav-button"} on:click={() => {navButtonClick("sea_creature")}}>
                <Icons name="seacreature" class="filter-icon"/>
            </button>
        {/if}
    </div>
    <div class="right">
        <button class="caughtbutton { filters.markAsCaught ? 'filter-button active' : 'filter-button' }" on:click={markAsCaughtToggle}>
            <h6 class="mb-0 center">
                <Icons name="caught" class="button-icon-small" style="margin-right: .3em" viewbox=128/>
                Mark as caught
            </h6>
        </button>
    </div>
</div>

<hr style="margin-top: -1.1em; position: relative">

<div class="pt-3 pb-4">
    <div class="center">
        <button class={filters.all ? "filter-button active" : "filter-button"} on:click={() => {filterButtonClick(true)}}>
            <h5 class="button-text center"><CalendarFill style="margin-right: .5em"/>All</h5>
        </button>
        <button class={!filters.all && currentTime() === filters.time && currentMonth() === filters.month && !filters.ignoreTime ? "filter-button active" : "filter-button"} on:click={() => {filterButtonClick(false)}}>
            <h5 class="button-text center"><CalendarEventFill style="margin-right: .5em"/>Current</h5>
        </button>
    </div>

    {#if !filters.all}
        <div class="center range-container-parent">
            <div class="range-container">
                <h3 class="mb-0">{monthNames[filters.month]}</h3>
                <input type="range" id="month" name="month" class="range-slider" min="1" max="12" bind:value={filters.month}/>
            </div>
            <div class="range-container">
                <h3 class="mb-0">{filters.ignoreTime ? "-" : `${filters.time}:00`}</h3>
                <input type="range" id="time" name="time" class="range-slider" min="0" max="23" bind:value={filters.time} disabled={filters.ignoreTime}/>
            </div>
        </div>

        <div class="center">
            <button class={filters.ignoreTime ? "filter-button active" : "filter-button"} on:click={ignoreTimeToggle}>
                <h5 class="center"><ClockFill style="margin-right: .5em"/> Ignore time</h5>
            </button>
        </div>

        <div class="center mt-2">
            <button class={filters.hideCaught ? "filter-button active" : "filter-button"} on:click={hideCaughtToggle}>
                <h5 class="center"><EyeSlashFill width=20 height=20 style="margin-right: .5em"/>Hide caught</h5>
            </button>
        </div>
        {#if selectedGame === "newhorizons"}
            <div class="center mt-2">
                <button class={filters.northernHemisphere ? "filter-button active" : "filter-button"} on:click={() => {hemisphereToggle(true)}}>
                    <h5><CircleHalf style="vertical-align: unset; margin-right: .5em; transform: rotate(90deg)"/>North</h5>
                </button>
                <button class={!filters.northernHemisphere ? "filter-button active" : "filter-button"} on:click={() => {hemisphereToggle(false)}}>
                    <h5><CircleHalf style="vertical-align: unset; margin-right: .5em; transform: rotate(-90deg)"/>South</h5>
                </button>
            </div>
        {/if}
        {#if selectedGame === "newleaf"}
            <div class="center mt-2">
                <button class={filters.includeIsland ? "filter-button active" : "filter-button"} on:click={includeIslandToggle}>
                    <h5>Include Tortimer Island</h5>
                </button>
            </div>
            <div class="center pt-3">
                <img src={islandExclusive} alt="Tortimer Island exclusive" style="width: 1em; height: 1em; margin-right: .5em"><p class="mb-0">Tortimer Island exclusive</p>
            </div>
            <div class="center">
                <img src={islandAvailable} alt="Year-round on Tortimer Island" style="width: 1em; height: 1em; margin-right: .5em"><p class="mb-0">Year-round on Tortimer Island</p>
            </div>
        {/if}
    {/if}
    <Toaster/>
</div>

<style>
    .filter-tabs {
        display: flex;
        justify-content: space-between;
        align-items: center;
        max-width: 90vw;
        margin: 0 auto;
    }

    .filter-tabs > .left,
    .filter-tabs > .right {
        flex: 0 1 auto;
    }

    .filter-button {
        border: 2px solid var(--button-dark);
        border-radius: 500px;
        background-color: rgba(0, 0, 0, 0);
        width: fit-content !important;
        height: fit-content !important;
        margin: 0 1em 0 1em;
        padding: 4px 6px 4px 6px;
    }

    .filter-button:hover {
        transform: scale(1.1);
        border-radius: 500px; /* Large for pill look */
    }

    .filter-button>h5,
    .filter-button>h6 {
        margin: 0;
        padding: 0 10px 0 10px;  /* Override for h6 below */
        color: var(--text);
    }

    /* Padding override */
    .filter-button>h6 {
        padding: 0 4px 0 4px !important;
    }

    .filter-button.active {
        background-color: var(--button-dark);
        border-radius: 500px; /* Large for pill look */
    }

    .filter-button.active>h5,
    .filter-button.active>h6 {
        color: var(--text-light);
    }

    .range-container {
        width: 15em;
        margin: 2em 2.5em;
    }

    @media (max-width: 420px) {
        .range-container-parent {
            justify-content: space-around !important;
        }

        .range-container {
            width: 40%;
            margin: 2.5em 0;
        }
    }

    .range-slider {
        -webkit-appearance: none;
        appearance: none;
        padding: 0;
        margin: 0;
        width: 100%;
        height: 15px;
        border-radius: 5px;
        background: #000000;
        outline: none;
        opacity: 0.4;
        -webkit-transition: .2s;
        transition: opacity .2s;
    }

    .range-slider[disabled] {
        opacity: 0.05;
    }

    .range-slider:hover {
        opacity: 1;
    }

    .range-slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 18px;
        height: 25px;
        border-radius: 5px;
        background: #ffffff;
        border: 3px solid #000000;
        cursor: pointer;
    }

    .range-slider::-moz-range-thumb {
        width: 18px;
        height: 25px;
        border-radius: 10px;
        background: #ffffff;
        border: 3px solid #000000;
        cursor: pointer;
    }

    .nav-button {
        margin: 0 -1em 0 0;
        border: none;
        border-radius: 50%;
        background-color: var(--filter-tabs);
        width: 4.5em;
        height: 4.5em;
        text-align: center;
    }

    @media (max-width: 430px) {
        .nav-button { width: 3.5em; height: 3.5em; }
        .caughtbutton > h6 { font-size: .8rem; }
        .filter-tabs { max-width: 98vw; }
        hr { margin-top: -.6em !important }
    }

    @media (max-width: 320px) {
        .nav-button { width: 3em; height: 3em;}
    }

    .nav-button.active {
        filter: brightness(85%);
        border-bottom: none;
    }

    .nav-button:hover {
        filter: brightness(60%)
    }

</style>
