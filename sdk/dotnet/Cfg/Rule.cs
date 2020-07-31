// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Cfg
{
    /// <summary>
    /// Provides an AWS Config Rule.
    /// 
    /// &gt; **Note:** Config Rule requires an existing `Configuration Recorder` to be present. Use of `depends_on` is recommended (as shown below) to avoid race conditions.
    /// 
    /// ## Example Usage
    /// ### AWS Managed Rules
    /// 
    /// AWS managed rules can be used by setting the source owner to `AWS` and the source identifier to the name of the managed rule. More information about AWS managed rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_use-managed-rules.html).
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var role = new Aws.Iam.Role("role", new Aws.Iam.RoleArgs
    ///         {
    ///             AssumeRolePolicy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///     {
    ///       ""Action"": ""sts:AssumeRole"",
    ///       ""Principal"": {
    ///         ""Service"": ""config.amazonaws.com""
    ///       },
    ///       ""Effect"": ""Allow"",
    ///       ""Sid"": """"
    ///     }
    ///   ]
    /// }
    /// ",
    ///         });
    ///         var foo = new Aws.Cfg.Recorder("foo", new Aws.Cfg.RecorderArgs
    ///         {
    ///             RoleArn = role.Arn,
    ///         });
    ///         var rule = new Aws.Cfg.Rule("rule", new Aws.Cfg.RuleArgs
    ///         {
    ///             Source = new Aws.Cfg.Inputs.RuleSourceArgs
    ///             {
    ///                 Owner = "AWS",
    ///                 SourceIdentifier = "S3_BUCKET_VERSIONING_ENABLED",
    ///             },
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 foo,
    ///             },
    ///         });
    ///         var rolePolicy = new Aws.Iam.RolePolicy("rolePolicy", new Aws.Iam.RolePolicyArgs
    ///         {
    ///             Role = role.Id,
    ///             Policy = @"{
    ///   ""Version"": ""2012-10-17"",
    ///   ""Statement"": [
    ///   	{
    ///   		""Action"": ""config:Put*"",
    ///   		""Effect"": ""Allow"",
    ///   		""Resource"": ""*""
    /// 
    ///   	}
    ///   ]
    /// }
    /// ",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Custom Rules
    /// 
    /// Custom rules can be used by setting the source owner to `CUSTOM_LAMBDA` and the source identifier to the Amazon Resource Name (ARN) of the Lambda Function. The AWS Config service must have permissions to invoke the Lambda Function, e.g. via the `aws.lambda.Permission` resource. More information about custom rules can be found in the [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html).
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var exampleRecorder = new Aws.Cfg.Recorder("exampleRecorder", new Aws.Cfg.RecorderArgs
    ///         {
    ///         });
    ///         // ... other configuration ...
    ///         var exampleFunction = new Aws.Lambda.Function("exampleFunction", new Aws.Lambda.FunctionArgs
    ///         {
    ///         });
    ///         // ... other configuration ...
    ///         var examplePermission = new Aws.Lambda.Permission("examplePermission", new Aws.Lambda.PermissionArgs
    ///         {
    ///             Action = "lambda:InvokeFunction",
    ///             Function = exampleFunction.Arn,
    ///             Principal = "config.amazonaws.com",
    ///         });
    ///         // ... other configuration ...
    ///         var exampleRule = new Aws.Cfg.Rule("exampleRule", new Aws.Cfg.RuleArgs
    ///         {
    ///             Source = new Aws.Cfg.Inputs.RuleSourceArgs
    ///             {
    ///                 Owner = "CUSTOM_LAMBDA",
    ///                 SourceIdentifier = exampleFunction.Arn,
    ///             },
    ///         }, new CustomResourceOptions
    ///         {
    ///             DependsOn = 
    ///             {
    ///                 exampleRecorder,
    ///                 examplePermission,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Rule : Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the config rule
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Description of the rule
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A string in JSON format that is passed to the AWS Config rule Lambda function.
        /// </summary>
        [Output("inputParameters")]
        public Output<string?> InputParameters { get; private set; } = null!;

        /// <summary>
        /// The frequency that you want AWS Config to run evaluations for a rule that
        /// is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        /// </summary>
        [Output("maximumExecutionFrequency")]
        public Output<string?> MaximumExecutionFrequency { get; private set; } = null!;

        /// <summary>
        /// The name of the rule
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the config rule
        /// </summary>
        [Output("ruleId")]
        public Output<string> RuleId { get; private set; } = null!;

        /// <summary>
        /// Scope defines which resources can trigger an evaluation for the rule as documented below.
        /// </summary>
        [Output("scope")]
        public Output<Outputs.RuleScope?> Scope { get; private set; } = null!;

        /// <summary>
        /// Source specifies the rule owner, the rule identifier, and the notifications that cause
        /// the function to evaluate your AWS resources as documented below.
        /// </summary>
        [Output("source")]
        public Output<Outputs.RuleSource> Source { get; private set; } = null!;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Rule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Rule(string name, RuleArgs args, CustomResourceOptions? options = null)
            : base("aws:cfg/rule:Rule", name, args ?? new RuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Rule(string name, Input<string> id, RuleState? state = null, CustomResourceOptions? options = null)
            : base("aws:cfg/rule:Rule", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Rule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Rule Get(string name, Input<string> id, RuleState? state = null, CustomResourceOptions? options = null)
        {
            return new Rule(name, id, state, options);
        }
    }

    public sealed class RuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Description of the rule
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A string in JSON format that is passed to the AWS Config rule Lambda function.
        /// </summary>
        [Input("inputParameters")]
        public Input<string>? InputParameters { get; set; }

        /// <summary>
        /// The frequency that you want AWS Config to run evaluations for a rule that
        /// is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        /// </summary>
        [Input("maximumExecutionFrequency")]
        public Input<string>? MaximumExecutionFrequency { get; set; }

        /// <summary>
        /// The name of the rule
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Scope defines which resources can trigger an evaluation for the rule as documented below.
        /// </summary>
        [Input("scope")]
        public Input<Inputs.RuleScopeArgs>? Scope { get; set; }

        /// <summary>
        /// Source specifies the rule owner, the rule identifier, and the notifications that cause
        /// the function to evaluate your AWS resources as documented below.
        /// </summary>
        [Input("source", required: true)]
        public Input<Inputs.RuleSourceArgs> Source { get; set; } = null!;

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public RuleArgs()
        {
        }
    }

    public sealed class RuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the config rule
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Description of the rule
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A string in JSON format that is passed to the AWS Config rule Lambda function.
        /// </summary>
        [Input("inputParameters")]
        public Input<string>? InputParameters { get; set; }

        /// <summary>
        /// The frequency that you want AWS Config to run evaluations for a rule that
        /// is triggered periodically. If specified, requires `message_type` to be `ScheduledNotification`.
        /// </summary>
        [Input("maximumExecutionFrequency")]
        public Input<string>? MaximumExecutionFrequency { get; set; }

        /// <summary>
        /// The name of the rule
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the config rule
        /// </summary>
        [Input("ruleId")]
        public Input<string>? RuleId { get; set; }

        /// <summary>
        /// Scope defines which resources can trigger an evaluation for the rule as documented below.
        /// </summary>
        [Input("scope")]
        public Input<Inputs.RuleScopeGetArgs>? Scope { get; set; }

        /// <summary>
        /// Source specifies the rule owner, the rule identifier, and the notifications that cause
        /// the function to evaluate your AWS resources as documented below.
        /// </summary>
        [Input("source")]
        public Input<Inputs.RuleSourceGetArgs>? Source { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;

        /// <summary>
        /// A map of tags to assign to the resource.
        /// </summary>
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public RuleState()
        {
        }
    }
}
