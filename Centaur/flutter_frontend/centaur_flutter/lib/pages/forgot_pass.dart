import 'package:flutter/material.dart';
import 'package:centaur_flutter/pages/login_cliente.dart';
import 'package:centaur_flutter/theme.dart';
import 'package:centaur_flutter/widgets/text_button.dart';
import 'package:centaur_flutter/widgets/field.dart';

class ForgotPassPage extends StatelessWidget {
  const ForgotPassPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: bgColor,
      body: Padding(
        padding: EdgeInsets.only(left: 30.0, right: 30.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              "Reset Password Sekarang",
              style: whiteTextStyle.copyWith(
                fontSize: 30,
                fontWeight: semiBold,
              ),
            ),
            SizedBox(
              height: 20,
            ),
            CustomField(
              iconUrl: 'assets/icon_email.png',
              hint: 'Email',
              passfield: false,
            ),
            CustomTextButton(
              title: 'Reset Password',
              margin: EdgeInsets.only(top: 50),
            ),
            Container(
              margin: EdgeInsets.only(
                top: 30,
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
                      "Kembali Ke Halaman Login",
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
      ),
    );
  }
}