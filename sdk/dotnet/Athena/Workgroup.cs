// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Athena
{
    /// <summary>
    /// Provides an Athena Workgroup.
    /// 
    /// 
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/athena_workgroup.html.markdown.
    /// </summary>
    public partial class Workgroup : Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the workgroup
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Configuration block with various settings for the workgroup. Documented below.
        /// </summary>
        [Output("configuration")]
        public Output<Outputs.WorkgroupConfiguration?> Configuration { get; private set; } = null!;

        /// <summary>
        /// Description of the workgroup.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        /// </summary>
        [Output("forceDestroy")]
        public Output<bool?> ForceDestroy { get; private set; } = null!;

        /// <summary>
        /// Name of the workgroup.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        /// </summary>
        [Output("state")]
        public Output<string?> State { get; private set; } = null!;

        /// <summary>
        /// Key-value mapping of resource tags for the workgroup.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Workgroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Workgroup(string name, WorkgroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws:athena/workgroup:Workgroup", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Workgroup(string name, Input<string> id, WorkgroupState? state = null, CustomResourceOptions? options = null)
            : base("aws:athena/workgroup:Workgroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Workgroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Workgroup Get(string name, Input<string> id, WorkgroupState? state = null, CustomResourceOptions? options = null)
        {
            return new Workgroup(name, id, state, options);
        }
    }

    public sealed class WorkgroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with various settings for the workgroup. Documented below.
        /// </summary>
        [Input("configuration")]
        public Input<Inputs.WorkgroupConfigurationArgs>? Configuration { get; set; }

        /// <summary>
        /// Description of the workgroup.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        /// </summary>
        [Input("forceDestroy")]
        public Input<bool>? ForceDestroy { get; set; }

        /// <summary>
        /// Name of the workgroup.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags for the workgroup.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public WorkgroupArgs()
        {
        }
    }

    public sealed class WorkgroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the workgroup
        /// </summary>
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// Configuration block with various settings for the workgroup. Documented below.
        /// </summary>
        [Input("configuration")]
        public Input<Inputs.WorkgroupConfigurationGetArgs>? Configuration { get; set; }

        /// <summary>
        /// Description of the workgroup.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The option to delete the workgroup and its contents even if the workgroup contains any named queries.
        /// </summary>
        [Input("forceDestroy")]
        public Input<bool>? ForceDestroy { get; set; }

        /// <summary>
        /// Name of the workgroup.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// State of the workgroup. Valid values are `DISABLED` or `ENABLED`. Defaults to `ENABLED`.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// Key-value mapping of resource tags for the workgroup.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public WorkgroupState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class WorkgroupConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
        /// </summary>
        [Input("bytesScannedCutoffPerQuery")]
        public Input<int>? BytesScannedCutoffPerQuery { get; set; }

        /// <summary>
        /// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
        /// </summary>
        [Input("enforceWorkgroupConfiguration")]
        public Input<bool>? EnforceWorkgroupConfiguration { get; set; }

        /// <summary>
        /// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
        /// </summary>
        [Input("publishCloudwatchMetricsEnabled")]
        public Input<bool>? PublishCloudwatchMetricsEnabled { get; set; }

        /// <summary>
        /// Configuration block with result settings. Documented below.
        /// </summary>
        [Input("resultConfiguration")]
        public Input<WorkgroupConfigurationResultConfigurationArgs>? ResultConfiguration { get; set; }

        public WorkgroupConfigurationArgs()
        {
        }
    }

    public sealed class WorkgroupConfigurationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
        /// </summary>
        [Input("bytesScannedCutoffPerQuery")]
        public Input<int>? BytesScannedCutoffPerQuery { get; set; }

        /// <summary>
        /// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
        /// </summary>
        [Input("enforceWorkgroupConfiguration")]
        public Input<bool>? EnforceWorkgroupConfiguration { get; set; }

        /// <summary>
        /// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
        /// </summary>
        [Input("publishCloudwatchMetricsEnabled")]
        public Input<bool>? PublishCloudwatchMetricsEnabled { get; set; }

        /// <summary>
        /// Configuration block with result settings. Documented below.
        /// </summary>
        [Input("resultConfiguration")]
        public Input<WorkgroupConfigurationResultConfigurationGetArgs>? ResultConfiguration { get; set; }

        public WorkgroupConfigurationGetArgs()
        {
        }
    }

    public sealed class WorkgroupConfigurationResultConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with encryption settings. Documented below.
        /// </summary>
        [Input("encryptionConfiguration")]
        public Input<WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs>? EncryptionConfiguration { get; set; }

        /// <summary>
        /// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
        /// </summary>
        [Input("outputLocation")]
        public Input<string>? OutputLocation { get; set; }

        public WorkgroupConfigurationResultConfigurationArgs()
        {
        }
    }

    public sealed class WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
        /// </summary>
        [Input("encryptionOption")]
        public Input<string>? EncryptionOption { get; set; }

        /// <summary>
        /// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        public WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs()
        {
        }
    }

    public sealed class WorkgroupConfigurationResultConfigurationEncryptionConfigurationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
        /// </summary>
        [Input("encryptionOption")]
        public Input<string>? EncryptionOption { get; set; }

        /// <summary>
        /// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
        /// </summary>
        [Input("kmsKeyArn")]
        public Input<string>? KmsKeyArn { get; set; }

        public WorkgroupConfigurationResultConfigurationEncryptionConfigurationGetArgs()
        {
        }
    }

    public sealed class WorkgroupConfigurationResultConfigurationGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration block with encryption settings. Documented below.
        /// </summary>
        [Input("encryptionConfiguration")]
        public Input<WorkgroupConfigurationResultConfigurationEncryptionConfigurationGetArgs>? EncryptionConfiguration { get; set; }

        /// <summary>
        /// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
        /// </summary>
        [Input("outputLocation")]
        public Input<string>? OutputLocation { get; set; }

        public WorkgroupConfigurationResultConfigurationGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class WorkgroupConfiguration
    {
        /// <summary>
        /// Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
        /// </summary>
        public readonly int? BytesScannedCutoffPerQuery;
        /// <summary>
        /// Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
        /// </summary>
        public readonly bool? EnforceWorkgroupConfiguration;
        /// <summary>
        /// Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
        /// </summary>
        public readonly bool? PublishCloudwatchMetricsEnabled;
        /// <summary>
        /// Configuration block with result settings. Documented below.
        /// </summary>
        public readonly WorkgroupConfigurationResultConfiguration? ResultConfiguration;

        [OutputConstructor]
        private WorkgroupConfiguration(
            int? bytesScannedCutoffPerQuery,
            bool? enforceWorkgroupConfiguration,
            bool? publishCloudwatchMetricsEnabled,
            WorkgroupConfigurationResultConfiguration? resultConfiguration)
        {
            BytesScannedCutoffPerQuery = bytesScannedCutoffPerQuery;
            EnforceWorkgroupConfiguration = enforceWorkgroupConfiguration;
            PublishCloudwatchMetricsEnabled = publishCloudwatchMetricsEnabled;
            ResultConfiguration = resultConfiguration;
        }
    }

    [OutputType]
    public sealed class WorkgroupConfigurationResultConfiguration
    {
        /// <summary>
        /// Configuration block with encryption settings. Documented below.
        /// </summary>
        public readonly WorkgroupConfigurationResultConfigurationEncryptionConfiguration? EncryptionConfiguration;
        /// <summary>
        /// The location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
        /// </summary>
        public readonly string? OutputLocation;

        [OutputConstructor]
        private WorkgroupConfigurationResultConfiguration(
            WorkgroupConfigurationResultConfigurationEncryptionConfiguration? encryptionConfiguration,
            string? outputLocation)
        {
            EncryptionConfiguration = encryptionConfiguration;
            OutputLocation = outputLocation;
        }
    }

    [OutputType]
    public sealed class WorkgroupConfigurationResultConfigurationEncryptionConfiguration
    {
        /// <summary>
        /// Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
        /// </summary>
        public readonly string? EncryptionOption;
        /// <summary>
        /// For `SSE_KMS` and `CSE_KMS`, this is the KMS key Amazon Resource Name (ARN).
        /// </summary>
        public readonly string? KmsKeyArn;

        [OutputConstructor]
        private WorkgroupConfigurationResultConfigurationEncryptionConfiguration(
            string? encryptionOption,
            string? kmsKeyArn)
        {
            EncryptionOption = encryptionOption;
            KmsKeyArn = kmsKeyArn;
        }
    }
    }
}
