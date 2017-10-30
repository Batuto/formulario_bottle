%rebase ./mysite/views/base.tpl page_title="Edit person"
<form action="/edit{{no}}" method="POST">
    <label>Name</label><br/>
    <input type="text" name="name" size="20" value="{{rec[1]}}" required pattern="(([a-z]|[A-Z])+[ ]?)+"><br/><br/>
    <label>Lastname</label><br/>
    <input type="text" name="last_name" size="20" value="{{rec[2]}}" required pattern="(([a-z]|[A-Z])+[ ]?)+"><br/><br/>
    <label>Bio</label><br/>
    <textarea name="bio" rows="10" cols="30" required>{{rec[3]}}</textarea><br/><br/>
    <label>Age</label><br/>
    <input type="number" name="age" size="2" value="{{rec[4]}}" required pattern="\d{3}"><br/><br/>
    <label>RegDate</label>
    <input type="text" name="regdatetime" size="25" value="{{rec[5]}}" required pattern="\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}:\d{2}.\d{6}"><br/><br/>

    <input type="submit" name="save" value="Save">
    <input type="button" name="" value="Cancel" onClick=window.history.back()>

</form>
<br>
