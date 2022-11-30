var stud_firstname = 'Student FN';
var stud_lastname = 'Student LN';
var stud_email =
  'student_' +
  Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, '')
    .substr(0, 9) +
  '@email.com';
var stud_password = (Math.random().toString(36) + '00000000000000000').slice(2, 12);

var teach_firstname = 'Teacher FN';
var teach_lastname = 'Teacher LN';
var teach_email =
  'teacher_' +
  Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, '')
    .substr(0, 9) +
  '@email.com';
var teach_password = (Math.random().toString(36) + '00000000000000000').slice(2, 12);

describe('Register student', () => {
  it('Test student register button', () => {
    cy.visit('/accounts/');
    cy.wait(500);
    cy.contains("I'm a student").click();
    cy.wait(500);
    cy.url().should('include', '/accounts/signup/student');
  });
  it('Test student register form', () => {
    cy.visit('/accounts/signup/student/');
    cy.get('form');
    cy.get('input[name = "first_name"]').type(stud_firstname);
    cy.wait(500);
    cy.get('input[name = "last_name"]').type(stud_lastname);
    cy.wait(500);
    cy.get('input[name = "email"]').type(stud_email);
    cy.wait(500);
    cy.get('input[name = "password1"]').type(stud_password);
    cy.wait(500);
    cy.get('input[name = "password2"]').type(stud_password);
    cy.wait(500);
    cy.contains('Register').click();
    //after clicking should redirect to homepage
    cy.url().should('include', '/');
  });
});

describe('Register teacher', () => {
  it('Test teacher register button', () => {
    cy.visit('/accounts/');
    cy.contains("I'm a teacher").click();
    cy.url().should('include', '/accounts/signup/teacher');
  });
  it('Test Register Form', () => {
    cy.visit('/accounts/signup/teacher/');
    cy.get('form');
    cy.get('input[name = "first_name"]').type(teach_firstname);
    cy.wait(500);
    cy.get('input[name = "last_name"]').type(teach_lastname);
    cy.wait(500);
    cy.get('input[name = "email"]').type(teach_email);
    cy.wait(500);
    cy.get('input[name = "password1"]').type(teach_password);
    cy.wait(500);
    cy.get('input[name = "password2"]').type(teach_password);
    cy.wait(500);
    cy.contains('Register').click();
    //after clicking should redirect to homepage
    cy.url().should('include', '/');
  });
});

describe('Student Login and Logout', () => {
  it('Test Login Form', () => {
    cy.visit('/accounts/login');
    cy.get('input[name = "username"]').type(stud_email);
    cy.get('input[name = "password"]').type(stud_password);
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Test Logout Click', () => {
    //test logout hyperlink
    cy.contains(stud_email).click();
    cy.wait(500);
    cy.contains('Log out').click();
    cy.contains('Sign in');
  });
});

describe('Teacher Login and Logout', () => {
  it('Test Login Form', () => {
    cy.visit('/accounts/login');
    cy.wait(500);
    cy.get('input[name = "username"]').type(teach_email);
    cy.wait(500);
    cy.get('input[name = "password"]').type(teach_password);
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Test Logout Click', () => {
    //test logout hyperlink
    cy.contains(teach_email).click();
    cy.wait(500);
    cy.contains('Log out').click();
    cy.contains('Sign in');
  });
});

describe('Teacher: Create Questions', () => {
  beforeEach(() => {
    cy.visit('/accounts/login');
    cy.wait(500);
    cy.get('input[name = "username"]').type(teach_email);
    cy.wait(500);
    cy.get('input[name = "password"]').type(teach_password);
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Test Create Question Button', () => {
    cy.visit('/');
    cy.contains('Create Question');
  });
  it('Add: Two Questions', () => {
    cy.visit('/question/add');
    cy.wait(500);
    cy.get('input[name = "question_text"]').type('Sample question 1');
    cy.wait(500);
    cy.get('form').submit();
    cy.visit('/question/add');
    cy.get('input[name = "question_text"]').type('Sample question 2');
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Test Add Choice Button', () => {
    cy.visit('/1');
    cy.contains('View Polling Result');
    cy.contains('Add choice').click();
  });
  it('Add: Choices for Question 1', () => {
    cy.visit('/1/choice/add');
    cy.wait(500);
    cy.get('input[name = "choice_text"]').type('Choice 1');
    cy.get('form').submit();
    cy.visit('/1/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 2');
    cy.get('form').submit();
    cy.visit('/1/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 3');
    cy.get('form').submit();
    cy.visit('/1/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 4');
    cy.get('form').submit();
  });
  it('Add: Choices for Question 2', () => {
    cy.visit('/2/choice/add');
    cy.wait(500);
    cy.get('input[name = "choice_text"]').type('Choice 1');
    cy.get('form').submit();
    cy.visit('/2/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 2');
    cy.get('form').submit();
    cy.visit('/2/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 3');
    cy.get('form').submit();
    cy.visit('/2/choice/add');
    cy.get('input[name = "choice_text"]').type('Choice 4');
    cy.get('form').submit();
  });
});

describe('Student: Make a poll', () => {
  beforeEach(() => {
    cy.visit('/accounts/login');
    cy.wait(500);
    cy.get('input[name = "username"]').type(stud_email);
    cy.wait(500);
    cy.get('input[name = "password"]').type(stud_password);
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Available polls', () => {
    cy.visit('/');
    cy.contains('Available Polls');
    cy.wait(500);
    cy.contains('Sample question 1').click();
    cy.url().should('include', '/1');
  });
  it('View Choices', () => {
    cy.visit('/1');
    cy.wait(500);
    cy.contains('Choice 1');
    cy.contains('Choice 2');
    cy.contains('Choice 3');
    cy.contains('Choice 4');
    cy.wait(500);
    cy.get('input[id = "choice4"]').click();
    cy.wait(500);
    cy.get('form').submit();
  });
  it('View Results', () => {
    cy.visit('/1/results');
    cy.contains('Choice 1 -- 0 votes');
    cy.contains('Choice 2 -- 0 votes');
    cy.contains('Choice 3 -- 0 votes');
    cy.contains('Choice 4 -- ');
  });
});

describe('RBAC: Anonymous', () => {
  it('Available polls', () => {
    cy.visit('/');
    cy.wait(500);
    cy.contains('Available Polls');
  });
  it('View Choices', () => {
    cy.visit('/1');
    cy.wait(500);
    cy.url().should('include', '/accounts/login/?next=/');
  });
  it('View Results', () => {
    cy.visit('/1/results');
    cy.url().should('include', '/accounts/login/?next=/');
    cy.contains('Login');
  });
});

describe('RBAC: Student', () => {
  beforeEach(() => {
    cy.visit('/accounts/login');
    cy.wait(500);
    cy.get('input[name = "username"]').type(stud_email);
    cy.wait(500);
    cy.get('input[name = "password"]').type(stud_password);
    cy.wait(500);
    cy.get('form').submit();
  });
  it('Add Question', () => {
    cy.visit('/question/add');
    cy.wait(500);
    cy.url().should('include', '/');
    cy.contains(stud_email);
  });
  it('Add Choice', () => {
    cy.visit('/');
    cy.wait(500);
    cy.contains(stud_email);
  });
});
