<script>
    import CritterContainer from "./components/CritterContainer.svelte";
    import Filters from "./components/Filters.svelte";
    import Footer from "./components/Footer.svelte";
    import Header from "./components/Header.svelte";

    import { currentMonth, currentTime} from "./utils"

    export let selectedGame = "newhorizons";
    export let filters = {
        "crittertype": "bug",
        "month": currentMonth(),
        "time": currentTime(),
        "all": false,
        "ignoreTime": false,
        "includeIsland": false,
        "markAsCaught": false,
        "hideCaught": false,
        "northernHemisphere": true,
    };

    export let darkMode = false;

</script>

<div class="main {darkMode ? 'dark' : 'light'}">
    <Header bind:selectedGame bind:darkMode/>

    <CritterContainer bind:selectedGame bind:filters bind:darkMode/>

    <Filters bind:selectedGame bind:filters/>

    <Footer/>
</div>

<style>
    .main {
        color: var(--text) !important;
	    background-color: var(--bg) !important;
        min-height: 100vh;
    }

    /* Colors on modal hard coded because of svelte weirdness */
    .light {
        --bg: #fff5e6;
        --bg-dark: #e7d5b9;
        --header: #588470;
        --header-light: #f2f6f3;
        --filter-tabs: #BDC49C;
        --button-dark: #354238;
        --text: #354238;
        --text-light: #f2f6f3;
    }

    .dark {
        --bg: #2c2a27;
        --bg-dark: #141312;
        --header: #23382f;
        --header-light: #2c2a27;
        --filter-tabs: #586138;
        --button-dark: #88ac91;
        --text: #e0ebe1;
        --text-light: #354238;
    }
</style>
