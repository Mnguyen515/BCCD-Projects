#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <regex.h>

// This Function checks the passwords' length an updates strength
int check_length(char *pwd, int strgth)
{
    int length = strlen(pwd);

    // Check for password length 
    // Return True if long enough
    if (length >= 8) 
    {
        strgth += 2;
        if (length >= 12) 
        {
            strgth += 2;
        }
    }
    // Return False if not long enough
    else
    {
        printf("\nThe password is not long enough!\n");
        printf("Make sure the password is at least 8 characters long.\n");
    }

    return strgth;
}

// This function checks for the types of characters in the password and updates strength
int check_char(char *pwd, int strgth)
{
    int hasLower = 0, hasUpper = 0, hasDigit = 0, hasSpecial = 0;

    // Check for character types
    for (int i = 0; i < strlen(pwd); i++) 
    {
        if (pwd[i] >= 'a' && pwd[i] <= 'z') 
        {
            hasLower += 1;
        } 

        else if (pwd[i] >= 'A' && pwd[i] <= 'Z') 
        {
            hasUpper += 1;
        } 

        else if (pwd[i] >= '0' && pwd[i] <= '9') 
        {
            hasDigit += 1;
        } 

        else if (pwd[i] >= '!' && pwd[i] <= '/')
        {
            hasSpecial += 1;
        }

        else if (pwd[i] >= '[' && pwd[i] <= '_')
        {
            hasSpecial += 1;
        }

        else if (pwd[i] >= ':' && pwd[i] <= '?')
        {
            hasSpecial += 1;
        }
        else if (pwd[i] >= '{' && pwd[i] <= '~')
        {
            hasSpecial += 1;
        }
    }

    if(hasLower == 0)
    {
        printf("\nThe password does not contain any lowercase letters.\n");
        printf("Add more lowercase letters to increase password strength.\n");
    }

    if(hasUpper == 0)
    {
        printf("\nThe password does not contain any uppercase letters.\n");
        printf("Add more uppercase letters to increase password strength.\n");
    }

    if(hasDigit == 0)
    {
        printf("\nThe password does not contain any digits.\n");
        printf("Add more digits to increase password strength.\n");
    }

    if(hasSpecial == 0)
    {
        printf("\nThe password does not contain any special characters.\n");
        printf("Add more special characters to increase password strength.\n");
    }

    // Update strength based on character types
    return strgth += hasLower + hasUpper + hasDigit + hasSpecial;
}

int main() {
    char password[100];
    int *length = 0, strength = 0;

    printf("Enter password: ");
    scanf("%s", password);

    strength = check_length(password, strength) + check_char(password, strength);

    if(strength < 10)
    {
        printf("\nPassword strength score: %d", strength);
        printf("\nYour password strength is poor.");
    }
    
    else if(strength >= 10 && strength < 20)
    {
        printf("\nPassword strength score: %d", strength);
        printf("\nYour password strength is moderate.");
    }

    else if (strength >= 20)
    {
        printf("\nPassword strength score: %d", strength);
        printf("\nYour password strength is excellent.");
    }

    return 0;
}