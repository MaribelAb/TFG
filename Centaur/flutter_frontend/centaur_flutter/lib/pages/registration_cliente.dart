import 'package:centaur_flutter/api/auth/auth_api.dart';
import 'package:centaur_flutter/models/user_cubit.dart';
import 'package:centaur_flutter/models/user_model.dart';
import 'package:centaur_flutter/pages/home/client_home.dart';
//import 'package:centaur_flutter/pages/home/home_cliente.dart';
import 'package:flutter/material.dart';
import 'package:centaur_flutter/pages/login_cliente.dart';
import 'package:centaur_flutter/theme.dart';
import 'package:centaur_flutter/widgets/text_button.dart';
import 'package:centaur_flutter/widgets/field.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class SignUpClient extends StatefulWidget {
  const SignUpClient({Key? key}) : super(key: key);

  @override
  State<SignUpClient> createState() => _SignUpClientState();
}

class _SignUpClientState extends State<SignUpClient> {
  TextEditingController usernameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
  TextEditingController emailController = TextEditingController();
  TextEditingController confirmPasswdController = TextEditingController();
 
 
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Registro cliente', style: tituloStyle(context),),
      ),
      backgroundColor: bgColor,
      body: ListView(
        padding: EdgeInsets.symmetric(
          horizontal: defaultMargin,
        ),
        children: [
          Container(
            margin: EdgeInsets.only(top: 100),
            child: Text(
              "Bienvenido a Centaur!",
              style: whiteTextStyle.copyWith(
                fontSize: 20,
                fontWeight: semiBold,
              ),
              textAlign: TextAlign.center,
            ),
          ),
          SizedBox(
            height: 5,
          ),
          CustomField(
            iconUrl: 'assets/icon_name.png',
            hint: 'Nombre de usuario',
            controller: usernameController,
            passfield: false,
          ),
          CustomField(
            iconUrl: 'assets/icon_email.png',
            hint: 'Email',
            controller: emailController,
            passfield: false,
          ),
          CustomField(
            iconUrl: 'assets/icon_password.png',
            hint: 'Contraseña',
            controller: passwordController,
            passfield: true,
          ),
          CustomField(
            iconUrl: 'assets/icon_password.png',
            hint: 'Confirma contraseña',
            controller: confirmPasswdController,
            passfield: true,
          ),
          CustomTextButton(
            title: 'Regístrate',
            margin: EdgeInsets.only(top: 50),
            onTap: () async {
              List<dynamic> authRes = await registerUser(
                usernameController.text,
                emailController.text,
                passwordController.text,
                confirmPasswdController.text,
              );

              if (authRes[0] == null) {
                
                showDialog(
                  context: context,
                  builder: (context) {
                    return Dialog(
                      child: Container(
                        alignment: Alignment.center,
                        height: 200,
                        width: 250,
                        decoration: BoxDecoration(),
                        child: Text(authRes[1]),
                      ),
                    );
                  },
                );
              } else {
                
                if (authRes[0] is User) {
                  User user = authRes[0] as User;
                  List<String> groupnames = ['Client'];
                  user.groups = groupnames;
                  context.read<UserCubit>().emit(user);
                  Navigator.of(context).push(MaterialPageRoute(
                    builder: (context) {
                      return ClientHome();
                    },
                  ));
                }
              }
            },
          ),

          Container(
            margin: EdgeInsets.only(
              top: 40,
              bottom: 74,
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                TextButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => SignInClient()),
                    );
                  },
                  child: Text(
                    "¿Ya tienes cuenta? Inicia sesión",
                    style: whiteTextStyle.copyWith(
                      fontSize: 16,
                      fontWeight: semiBold,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}