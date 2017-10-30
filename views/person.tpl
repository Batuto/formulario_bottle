%rebase('base.tpl', page_title="People List")
<div class="people_name">
    <h2>{{name}}</h2>
    <br/>
    <h3>{{last_name}}</h3>
</div>

<div class="reg_date">
    Registered: {{regdatetime}}
</div>

<div class="bio">
    <p>{{bio}}</p>
    <p><b>Age:</b> {{age}}</p>
</div>
<button onClick=window.history.back()>Return</button>
<button onclick="location.href='/edit{{pid}}'">Edit</button>
