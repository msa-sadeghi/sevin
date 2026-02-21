const appEl = document.getElementById("app")

function createApp(rootEl){

    rootEl.innerHTML = `
    <div class="row">
        <input id="q" placeholder="search..."/>
        <button id="sample">sample</button>
        <button id="clear">clear</button>
    </div>
    <div style="margin-top:10px">
    <textarea id="text" placeholder="new note..."></textarea>
    <div class="row">
        <button id="add">add</button>
        <span class="meta" id="status"></span>
    </div>
    </div>
    <ul id="list"></ul>
    `
}

createApp(appEl)