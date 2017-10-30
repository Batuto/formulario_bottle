%rebase('base.tpl', page_title="New person")
<h3>Add new people to the People list</h3>
<form action="/new" method="POST">
    <label>Name</label>
    <br/>
    <input type="text" name="name" size="20"/>
    <br/>
    <label>Lastname</label>
    <br/>
    <input type="text" name="last_name" size="20"/>
    <br/>
    <label>Age</label>
    <br/>
    <input type="text" name="age" size="2"/>
    <br/>
    <label>Bio</label>
    <br/>
    <textarea name="bio" rows="10" cols="30"></textarea>
    <br/>
    <input type="submit" name="save" value="Save">
    <input type="button" name="cancel" value="Cancel" onclick="parent.location='/'">
</form>
