%rebase('base.tpl', page_title="Edit person")
<form action="/edit{{no}}" method="POST">
    <label>Name</label><br/>
    <input type="text" name="name" size="20" value="{{rec[1]}}"><br/><br/>
    <label>Lastname</label><br/>
    <input type="text" name="last_name" size="20" value="{{rec[2]}}"><br/><br/>
    <label>Bio</label><br/>
    <textarea name="desc" rows="10" cols="30">{{rec[3]}}</textarea><br/><br/>
    <label>Age</label><br/>
    <input type="text" name="age" size="2" value="{{rec[4]}}"><br/><br/>
    <label>RegDate</label>
    <input type="text" name="regdatetime" size="25" value="{{rec[5]}}"><br/><br/>

    <input type="submit" name="save" value="Save">
    <input type="button" name="" value="Cancel" onClick=window.history.back()>

</form>
<br>
