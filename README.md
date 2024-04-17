**The pipeline does**

<br>Extract data from news api :author, content, source,title ,puplish_date since 24 hours ago,</br>
<br>Transform data: lower all  characters,convert datatype for columns, etc.</br>
<br>Load data into a Sqlite database.</br>

**Pipeline task graph:**



                                     news_etl_script
    
    ╭──────────────╮     ╭──────────────╮     ╭────────────────╮    
    │ extract_task │ ──▶ │transform_task│ ──▶ │   load_task    │
    ╰──────────────╯     ╰──────────────╯     ╰────────────────╯     
