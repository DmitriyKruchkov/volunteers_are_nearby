from flask import Blueprint, render_template, redirect
from flask_login import login_user, logout_user, login_required, current_user
from form.account_editform import AccountEditForm
from form.account_password_form import AccountPasswordForm
from services.roles import getRole
from services.users import getUserByEmail, checkUsers, addUserFromForm, loadNewData, changePassword
from form.loginform import LoginForm
from form.registerform import RegisterForm

user_router = Blueprint("users", __name__)


@user_router.route('/login', methods=['GET', 'POST'])
def login():
    """
        Обработка запросов на авторизацию. Проверка корректности логина и пароля.
        Если данные верны, то происходит вход в систему.

         Returns:
             html шаблон
        """
    form = LoginForm()
    if form.validate_on_submit():
        user = getUserByEmail(form.email.data)
        if user and user.check_password(form.password.data):
            # После добавления куков разкомментировать
            # login_user(user, remember=form.remember_me.data)
            login_user(user)
            return redirect("/events")
        return render_template(
            template_name_or_list='login.html',
            message="Неправильный логин или пароль",
            form=form
        )
    return render_template(
        template_name_or_list='login.html',
        title='Авторизация',
        form=form
    )


@user_router.route('/register', methods=['GET', 'POST'])
def reqister():
    """
        Регистрация нового пользователя. Валидация формы регистрации.
        Создание нового пользователя в базе данных при успешной валидации.

        :return: шаблон формы регистрации с сообщением об ошибке, если она есть
        """
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template(
                'register.html',
                title='Регистрация',
                form=form,
                message="Пароли не совпадают"
            )
        if checkUsers(email=form.email.data, nickname=form.nickname.data):
            return render_template(
                template_name_or_list='register.html',
                title='Регистрация',
                form=form,
                message="Такой пользователь уже есть"
            )
        addUserFromForm(form)
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@user_router.route('/logout')
@login_required
def logout():
    """
        Выход из системы. Деавторизация пользователя.

        :return: редирект на главную страницу
        """
    logout_user()
    return redirect("/")



@user_router.route('/account')
@user_router.route("/account/info")
@login_required
def account_info():
    role = getRole(current_user.mode_id)
    return render_template(
        template_name_or_list="account_info.html",
        role_name=role.name
    )


@user_router.route("/account/edit", methods=['GET', 'POST'])
@login_required
def account_edit():
    form = AccountEditForm()
    if form.validate_on_submit():
        loadNewData(form)
        return redirect("/account/info")
    form.auto_fill(current_user)
    return render_template("account_edit.html", form=form)


@user_router.route("/account/password", methods=['GET', 'POST'])
@login_required
def account_password():
    form = AccountPasswordForm()
    if form.validate_on_submit():
        if form.new_password.data != form.new_password_again.data:
            return render_template(
                template_name_or_list="account_password.html",
                form=form,
                message="Пароли не совпадают"
            )
        change_status = changePassword(form)
        if change_status:
            logout_user()
            return redirect("/login")
        return render_template(
            template_name_or_list="account_password.html",
            form=form,
            message="Неправильный пароль"
        )
    return render_template(
        template_name_or_list="account_password.html",
        form=form
    )
